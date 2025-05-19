import { useState, useEffect } from "react";
import Navbar from "@/layout/Navbar";
import EventoListener from "@/components/interaction/EventoListener";
import {
  fsmTransitions,
  NoraEvent,
  NoraState,
  EventLog,
} from "@/components/interaction/InteractionDef";

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
      if (!res.ok) throw new Error("Error en la respuesta del backend");

      const estadoNuevo = normalizaEstado(data.estado_actual);
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

  const isEventValid = (event: NoraEvent) => !!fsmTransitions[currentState][event];

  const formatTime = (date: Date) =>
    date.toLocaleTimeString([], {
      hour: "2-digit",
      minute: "2-digit",
      second: "2-digit",
    });

  useEffect(() => {
    const timeout = setTimeout(() => {
      fetch(`${import.meta.env.VITE_API_URL}/sensor/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
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
        .catch((err) => console.error("Error enviando sensor:", err));
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
          {/* Panel de interacción y sensores */}
          {/* FSM + EventLog */}
          {/* Aquí puedes seguir estructurando visualmente la interacción como lo hacías */}
        </div>
      </div>
    </div>
  );
};

export default NoraInteractionPage;
