import { useEffect } from "react";

type EventoFSM = {
  evento: string;
  nuevo_estado: string;
  descripcion?: string;
};

type Props = {
  onEventoRecibido: (evento: EventoFSM) => void;
};

const EventoListener: React.FC<Props> = ({ onEventoRecibido }) => {
  useEffect(() => {
    const socket = new WebSocket("ws://localhost:8000/ws/eventos/");

    socket.onopen = () => {
      console.log("✅ WebSocket conectado");
    };

    socket.onmessage = (event: MessageEvent) => {
      try {
        const data: EventoFSM = JSON.parse(event.data);
        console.log("📡 Evento FSM desde WebSocket:", data);
        onEventoRecibido(data);
      } catch (e) {
        console.error("❌ Error parseando evento FSM:", e);
      }
    };

    socket.onclose = () => {
      console.warn("🔌 WebSocket cerrado");
    };

    socket.onerror = (err) => {
      console.error("⚠️ Error WebSocket:", err);
    };

    return () => {
      socket.close();
    };
  }, [onEventoRecibido]);

  return null;
};

export default EventoListener;
