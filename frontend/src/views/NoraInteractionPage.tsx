import React, { useState, useEffect, useCallback, useRef } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Button } from "@/ui/button";
import { cn } from "@/lib/utils";
import Navbar from "@/layout/Navbar";
import EventoListener from "@/components/interaction/EventoListener";

import {
  eventLabels,
  eventGroups,
  fsmTransitions,
  nodePositions,
  stateColors,
} from "@/components/interaction/InteractionDef";
import type {
  NoraEvent,
  NoraState,
  EventLog,
} from "@/components/interaction/InteractionDef";

/**
 * Página principal de simulación e interacción de la FSM de NORA.
 *
 * Responsabilidades:
 * - Mostrar el estado actual del sistema.
 * - Permitir el envío manual de eventos al backend.
 * - Escuchar eventos emitidos por WebSocket.
 * - Reflejar visualmente transiciones y registrar un log reciente.
 * - Enviar lecturas simuladas del sensor de temperatura.
 */
const NoraInteractionPage: React.FC = () => {
  const [currentState, setCurrentState] = useState<NoraState>("INACTIVO");
  const [eventLog, setEventLog] = useState<EventLog[]>([]);
  const [temperature, setTemperature] = useState<number>(22.0);
  const [highlightedTransition, setHighlightedTransition] = useState<{
    from: NoraState;
    to: NoraState;
  } | null>(null);

  const currentStateRef = useRef<NoraState>(currentState);
  const transitionTimeoutRef = useRef<number | null>(null);
  const clearHighlightTimeoutRef = useRef<number | null>(null);

  const apiBaseUrl = (import.meta.env.VITE_API_URL ?? "http://localhost:8000").replace(
    /\/+$/,
    ""
  );

  console.log("[PAGE] Render NoraInteractionPage", {
    currentState,
    eventLogLength: eventLog.length,
    temperature,
    highlightedTransition,
  });

  /**
   * Mantiene sincronizada una referencia mutable con el estado actual,
   * para poder leerlo desde callbacks estables sin recrearlos.
   */
  useEffect(() => {
    currentStateRef.current = currentState;
    console.log("[STATE] currentState actualizado:", currentState);
  }, [currentState]);

  /**
   * Traza específica para saber si cambia el log.
   */
  useEffect(() => {
    console.log("[STATE] eventLog actualizado:", eventLog);
  }, [eventLog]);

  /**
   * Traza específica para saber si cambia el resaltado.
   */
  useEffect(() => {
    console.log("[STATE] highlightedTransition actualizado:", highlightedTransition);
  }, [highlightedTransition]);

  /**
   * Limpia timeouts pendientes cuando el componente se desmonta.
   */
  useEffect(() => {
    return () => {
      console.log("[LIFECYCLE] Unmount NoraInteractionPage");
      if (transitionTimeoutRef.current !== null) {
        window.clearTimeout(transitionTimeoutRef.current);
      }
      if (clearHighlightTimeoutRef.current !== null) {
        window.clearTimeout(clearHighlightTimeoutRef.current);
      }
    };
  }, []);

  /**
   * Normaliza nombres de estado provenientes del backend
   * hacia el conjunto de estados usado por el frontend.
   *
   * @param estado Estado recibido desde backend.
   * @param fallback Estado de respaldo si no llega ninguno.
   * @returns Estado normalizado del dominio del frontend.
   */
  const normalizaEstado = useCallback(
    (estado?: string, fallback: NoraState = "INACTIVO"): NoraState => {
      const mapeo: Record<string, NoraState> = {
        ACTIVADO: "ACTIVO",
        ESCUCHA: "ESCUCHANDO",
      };

      const normalizado = !estado ? fallback : ((mapeo[estado] || estado) as NoraState);

      console.log("[FSM] normalizaEstado", {
        entrada: estado,
        fallback,
        salida: normalizado,
      });

      return normalizado;
    },
    []
  );

  /**
   * Aplica una transición confirmada por backend al estado visual local.
   * También registra el evento y activa el resaltado temporal.
   *
   * @param evento Evento que provoca la transición.
   * @param fromState Estado origen.
   * @param toState Estado destino.
   */
  const aplicarTransicionConfirmada = useCallback(
    (evento: NoraEvent, fromState: NoraState, toState: NoraState) => {
      console.log("[FSM] aplicarTransicionConfirmada IN", {
        evento,
        fromState,
        toState,
        currentStateRef: currentStateRef.current,
      });

      if (!toState) {
        console.warn("[FSM] toState vacío, no se aplica transición");
        return;
      }

      if (transitionTimeoutRef.current !== null) {
        window.clearTimeout(transitionTimeoutRef.current);
      }

      if (clearHighlightTimeoutRef.current !== null) {
        window.clearTimeout(clearHighlightTimeoutRef.current);
      }

      if (fromState === toState) {
        console.log("[FSM] fromState === toState, actualizando solo currentState");
        setCurrentState(toState);
        currentStateRef.current = toState;
        return;
      }

      const newLog: EventLog = {
        id: Date.now(),
        event: evento,
        timestamp: new Date(),
        fromState,
        toState,
      };

      console.log("[FSM] Añadiendo log y resaltando transición", newLog);

      setEventLog((prev) => [newLog, ...prev].slice(0, 5));
      setHighlightedTransition({ from: fromState, to: toState });

      transitionTimeoutRef.current = window.setTimeout(() => {
        console.log("[FSM] Timeout transición completado. Nuevo estado:", toState);
        setCurrentState(toState);
        currentStateRef.current = toState;

        clearHighlightTimeoutRef.current = window.setTimeout(() => {
          console.log("[FSM] Limpiando highlightedTransition");
          setHighlightedTransition(null);
        }, 500);
      }, 500);
    },
    []
  );

  /**
   * Envía al backend un evento manual de FSM y aplica la transición
   * devuelta por la API HTTP.
   *
   * @param eventoActual Evento que se desea enviar.
   */
  const enviarEventoAlBackend = useCallback(
    async (eventoActual: NoraEvent) => {
      const estadoActual = currentStateRef.current;
      console.log("[HTTP] Enviando evento al backend:", {
        eventoActual,
        estadoActual,
      });

      try {
        const res = await fetch(`${apiBaseUrl}/fsm/event/`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            type: "fsm_event",
            evento: eventoActual,
            descripcion: "",
          }),
        });

        const data = await res.json();
        console.log("[HTTP] Respuesta del backend:", data);

        if (!res.ok) {
          throw new Error("Error en la respuesta del backend");
        }

        const estadoNuevo = normalizaEstado(data.estado_actual, estadoActual);

        console.log("[HTTP] Aplicando transición desde respuesta HTTP", {
          eventoActual,
          estadoActual,
          estadoNuevo,
        });

        aplicarTransicionConfirmada(eventoActual, estadoActual, estadoNuevo);
      } catch (error) {
        console.error("[HTTP] Fallo al enviar evento al backend:", error);
      }
    },
    [apiBaseUrl, aplicarTransicionConfirmada, normalizaEstado]
  );

  /**
   * Determina si un evento es válido para el estado actual de la FSM.
   *
   * @param event Evento a validar.
   * @returns `true` si la transición existe desde el estado actual.
   */
  const isEventValid = useCallback(
    (event: NoraEvent): boolean => {
      const valid = !!fsmTransitions[currentState][event];
      console.log("[FSM] isEventValid", { currentState, event, valid });
      return valid;
    },
    [currentState]
  );

  /**
   * Formatea una marca temporal para el log visual.
   *
   * @param date Fecha a formatear.
   * @returns Hora en formato HH:mm:ss.
   */
  const formatTime = useCallback((date: Date): string => {
    return date.toLocaleTimeString([], {
      hour: "2-digit",
      minute: "2-digit",
      second: "2-digit",
    });
  }, []);

  /**
   * Callback estable para procesar eventos recibidos por WebSocket.
   * Usa refs para acceder al estado actual sin recrearse en cada render.
   *
   * @param data Payload recibido desde el WebSocket.
   */
  const handleEventoRecibido = useCallback(
    (data: {
      evento: string;
      nuevo_estado?: string;
      estado_actual?: string;
      estado_anterior?: string;
      descripcion?: string;
    }) => {
      console.log("[WS->PAGE] Evento recibido en NoraInteractionPage:", data);

      const estadoActualRef = currentStateRef.current;
      const estadoNuevo = normalizaEstado(
        data.nuevo_estado ?? data.estado_actual,
        estadoActualRef
      );
      const estadoAnterior = normalizaEstado(
        data.estado_anterior,
        estadoActualRef
      );
      const evento = data.evento as NoraEvent;

      console.log("[WS->PAGE] Datos normalizados:", {
        estadoActualRef,
        estadoAnterior,
        estadoNuevo,
        evento,
      });

      aplicarTransicionConfirmada(evento, estadoAnterior, estadoNuevo);
    },
    [aplicarTransicionConfirmada, normalizaEstado]
  );

  /**
   * Envía periódicamente la lectura simulada del sensor cuando cambia
   * la temperatura o el estado actual.
   */
  useEffect(() => {
    const timeoutId = window.setTimeout(() => {
      console.log("[SENSOR] Enviando temperatura al backend", {
        temperature,
        current_state: currentStateRef.current,
      });

      fetch(`${apiBaseUrl}/fsm/sensor/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          sensor: "temperatura",
          value: temperature,
          current_state: currentStateRef.current,
        }),
      })
        .then((res) => res.json())
        .then((data) => {
          console.log("[SENSOR] Respuesta backend:", data);

          if (!data) {
            console.warn("[SENSOR] Respuesta vacía");
            return;
          }

          if (data.estado_actual) {
            const estadoActual = currentStateRef.current;
            const estadoNuevo = normalizaEstado(data.estado_actual, estadoActual);

            console.log("[SENSOR] Comparativa de estados:", {
              estadoActual,
              estadoNuevo,
              evento: data.evento,
            });

            if (estadoNuevo !== estadoActual && data.evento) {
              aplicarTransicionConfirmada(
                data.evento as NoraEvent,
                estadoActual,
                estadoNuevo
              );
            } else if (estadoNuevo !== estadoActual) {
              console.log("[SENSOR] Actualizando currentState sin evento:", estadoNuevo);
              setCurrentState(estadoNuevo);
              currentStateRef.current = estadoNuevo;
            }
          }
        })
        .catch((err) => {
          console.error("[SENSOR] Error enviando sensor:", err);
        });
    }, 500);

    return () => {
      window.clearTimeout(timeoutId);
    };
  }, [apiBaseUrl, temperature, currentState, aplicarTransicionConfirmada, normalizaEstado]);

  return (
    <div className="min-h-screen bg-black text-white font-['Roboto',sans-serif] px-6 pt-24">
      <Navbar />

      <EventoListener onEventoRecibido={handleEventoRecibido} />

      <div className="max-w-screen-xl mx-auto">
        <h1 className="text-3xl font-bold text-cyan-400 mb-6">
          NORA Interaction Simulator
        </h1>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          <div className="bg-[#1a1a1a] border border-gray-800 rounded-xl p-6 shadow-inner">
            <h2 className="text-xl font-semibold mb-4 text-cyan-300">
              Interaction Events
            </h2>

            {Object.entries(eventGroups).map(([group, events]) => (
              <div key={group} className="mb-6">
                <h3 className="text-md font-medium mb-2 text-cyan-200">{group}</h3>
                <div className="grid grid-cols-2 gap-2">
                  {events.map((evt) => (
                    <Button
                      key={evt}
                      onClick={() => enviarEventoAlBackend(evt)}
                      disabled={!isEventValid(evt)}
                      variant={isEventValid(evt) ? "default" : "outline"}
                      className={cn(
                        "text-sm px-3 py-2",
                        isEventValid(evt)
                          ? "hover:bg-cyan-600"
                          : "opacity-50 cursor-not-allowed"
                      )}
                    >
                      {eventLabels[evt]}
                    </Button>
                  ))}
                </div>
              </div>
            ))}

            <div className="bg-[#1a1a1a] border border-gray-800 rounded-xl p-6 shadow-inner">
              <h2 className="text-xl font-semibold mb-4 text-orange-400">Sensores</h2>
              <div className="mb-6">
                <label
                  htmlFor="sensor-temp"
                  className="block text-sm font-medium text-orange-300 mb-2"
                >
                  Temperatura ambiental: {temperature} °C
                </label>
                <input
                  id="sensor-temp"
                  type="range"
                  min={-10}
                  max={50}
                  step={0.5}
                  value={temperature}
                  onChange={(e) => setTemperature(parseFloat(e.target.value))}
                  className="w-full h-2 bg-gray-700 rounded-lg appearance-none cursor-pointer"
                />
              </div>
            </div>
          </div>

          <div className="lg:col-span-2 bg-[#1a1a1a] border border-gray-800 rounded-xl p-6 shadow-inner">
            <h2 className="text-xl font-semibold mb-4 text-cyan-300">System State</h2>

            <div className="relative h-96 mb-6 border border-slate-700 rounded-lg bg-black overflow-hidden">
              {Object.entries(nodePositions).map(([state, pos]) => {
                const isActive = state === currentState;

                return (
                  <motion.div
                    key={state}
                    className={cn(
                      "absolute rounded-full flex items-center justify-center shadow-md text-xs font-bold",
                      stateColors[state as NoraState],
                      isActive ? "w-16 h-16 ring-4 ring-white" : "w-12 h-12"
                    )}
                    style={{
                      left: `${pos.x}px`,
                      top: `${pos.y}px`,
                      transform: "translate(-50%, -50%)",
                    }}
                    animate={{ scale: isActive ? 1.2 : 1 }}
                    transition={{ type: "spring", stiffness: 300, damping: 20 }}
                  >
                    {state}
                  </motion.div>
                );
              })}

              <svg className="absolute inset-0 w-full h-full">
                {Object.entries(fsmTransitions).flatMap(([from, trans]) =>
                  Object.entries(trans).map(([event, to]) => {
                    const a = nodePositions[from as NoraState];
                    const b = nodePositions[to as NoraState];
                    const midX = (a.x + b.x) / 2;
                    const midY = (a.y + b.y) / 2;
                    const dx = b.x - a.x;
                    const dy = b.y - a.y;
                    const norm = Math.sqrt(dx * dx + dy * dy);

                    if (norm === 0) {
                      return null;
                    }

                    const offset = 30;
                    const offsetX = (-dy / norm) * offset;
                    const offsetY = (dx / norm) * offset;
                    const cx = midX + offsetX;
                    const cy = midY + offsetY;
                    const isHighlighted =
                      highlightedTransition?.from === from &&
                      highlightedTransition?.to === to;

                    return (
                      <path
                        key={`${from}-${event}-${to}`}
                        d={`M ${a.x} ${a.y} Q ${cx} ${cy} ${b.x} ${b.y}`}
                        fill="none"
                        stroke={isHighlighted ? "#22d3ee" : "#475569"}
                        strokeWidth={isHighlighted ? 2 : 1}
                        strokeDasharray={isHighlighted ? "none" : "5,5"}
                      />
                    );
                  })
                )}
              </svg>
            </div>

            <div>
              <h3 className="text-lg font-medium mb-3 text-cyan-200">Event Log</h3>
              <div className="bg-black border border-gray-700 rounded-xl p-4 max-h-48 overflow-y-auto">
                <AnimatePresence>
                  {eventLog.length > 0 ? (
                    eventLog.map((log) => (
                      <motion.div
                        key={log.id}
                        initial={{ opacity: 0, y: -10 }}
                        animate={{ opacity: 1, y: 0 }}
                        exit={{ opacity: 0 }}
                        className="mb-2 p-2 bg-[#1a1a1a] rounded border-l-4 border-cyan-500"
                      >
                        <div className="flex justify-between">
                          <span className="font-medium">{eventLabels[log.event]}</span>
                          <span className="text-slate-400 text-sm">
                            {formatTime(log.timestamp)}
                          </span>
                        </div>
                        <div className="text-sm text-slate-300">
                          {log.fromState} → {log.toState}
                        </div>
                      </motion.div>
                    ))
                  ) : (
                    <p className="text-slate-500 text-center">No events recorded</p>
                  )}
                </AnimatePresence>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default NoraInteractionPage;