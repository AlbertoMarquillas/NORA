import React, { useState, useEffect } from "react";
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
import type { NoraEvent, NoraState, EventLog } from "@/components/interaction/InteractionDef";

// Tu componente principal ahora solo tiene que importar y usar los elementos

const NoraInteractionPage = () => {
  const [currentState, setCurrentState] = useState<NoraState>("INACTIVO");
  const [eventLog, setEventLog] = useState<EventLog[]>([]);
  const [temperature, setTemperature] = useState<number>(22.0);
  const [highlightedTransition, setHighlightedTransition] = useState<{
    from: NoraState;
    to: NoraState;
  } | null>(null);

  const enviarEventoAlBackend = async (eventoActual: NoraEvent) => {
    console.log("Enviando evento al backend:", eventoActual, "desde", currentState);

    try {
      const res = await fetch(`${import.meta.env.VITE_API_URL}/evento/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          type: "fsm_event",
          evento: eventoActual,
          descripcion: "",
        }),
      });


      const data = await res.json();
      console.log("Respuesta del backend:", data);

      if (!res.ok) throw new Error("Error en la respuesta del backend");

      const estadoNuevo = normalizaEstado(data.estado_actual);

      console.log(
        "Estado nuevo recibido del backend:",
        estadoNuevo,
        "Estado actual:",
        currentState,
        "Evento actual:",
        eventoActual
      );

      console.log("TRANSICION:", fsmTransitions[currentState][eventoActual]);

      if (fsmTransitions[currentState][eventoActual] === estadoNuevo) {
        realizarTransicion(eventoActual);
      } else {
        console.warn("Evento válido pero transición no encontrada");
      }
    } catch (error) {
      console.error("Fallo al enviar evento al backend:", error);
    }
  };

  const normalizaEstado = (estado: string): NoraState => {
    const mapeo: Record<string, NoraState> = {
      ACTIVADO: "ACTIVO",
      ESCUCHA: "ESCUCHANDO",
    };
    return (mapeo[estado] || estado) as NoraState;
  };

  const realizarTransicion = (evento: NoraEvent) => {

    const nextState = fsmTransitions[currentState][evento];
    if (!nextState) return;

    const newLog: EventLog = {
      id: Date.now(),
      event: evento,
      timestamp: new Date(),
      fromState: currentState,
      toState: nextState,
    };

    setEventLog((prev) => [newLog, ...prev].slice(0, 5));
    setHighlightedTransition({ from: currentState, to: nextState });

    setTimeout(() => {
      setCurrentState(nextState);
      setTimeout(() => setHighlightedTransition(null), 500);
    }, 500);
  };

  const isEventValid = (event: NoraEvent) => {
    return !!fsmTransitions[currentState][event];
  };

  const formatTime = (date: Date) => {
    return date.toLocaleTimeString([], {
      hour: "2-digit",
      minute: "2-digit",
      second: "2-digit",
    });
  };

  useEffect(() => {
    const timeout = setTimeout(() => {
      fetch('${import.meta.env.VITE_API_URL}/sensor/', {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          sensor: "temperatura",
          value: temperature,
          current_state: currentState,
        }),
      })
        .then((res) => res.json())
        .then((data) => {
          if (data && data.evento_futuro && isEventValid(data.evento_futuro)) {
            realizarTransicion(data.evento_futuro);
          }
        })
        .catch((err) => {
          console.error("Error enviando sensor:", err);
        });
    }, 500);

    return () => clearTimeout(timeout);
  }, [temperature]);

  return (
    <div className="min-h-screen bg-black text-white font-['Roboto',sans-serif] px-6 pt-24">
      <Navbar />
      <EventoListener
        onEventoRecibido={(data) => {
          const estado = normalizaEstado(data.nuevo_estado);
          if (fsmTransitions[currentState][data.evento] === estado) {
            realizarTransicion(data.evento as NoraEvent);
          } else {
            console.warn("Transición inesperada (WebSocket):", data);
          }
        }}
      />
      <div className="max-w-screen-xl mx-auto">
        <h1 className="text-3xl font-bold text-cyan-400 mb-6">NORA Interaction Simulator</h1>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          <div className="bg-[#1a1a1a] border border-gray-800 rounded-xl p-6 shadow-inner">
            <h2 className="text-xl font-semibold mb-4 text-cyan-300">Interaction Events</h2>
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
                <label htmlFor="sensor-temp" className="block text-sm font-medium text-orange-300 mb-2">
                  Temperatura ambiental: {temperature} °C
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
                          <span className="font-medium">
                            {eventLabels[log.event]}
                          </span>
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