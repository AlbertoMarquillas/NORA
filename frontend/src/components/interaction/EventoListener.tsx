import { useEffect, useRef } from "react";

type EventoFSM = {
  evento: string;
  nuevo_estado?: string;
  estado_actual?: string;
  estado_anterior?: string;
  descripcion?: string;
};

type Props = {
  onEventoRecibido: (evento: EventoFSM) => void;
};

const EventoListener: React.FC<Props> = ({ onEventoRecibido }) => {
  const onEventoRecibidoRef = useRef(onEventoRecibido);

  useEffect(() => {
    onEventoRecibidoRef.current = onEventoRecibido;
  }, [onEventoRecibido]);

  useEffect(() => {
    const rawBaseUrl = import.meta.env.VITE_WS_BASE_URL ?? "ws://localhost:8000";
    const wsBaseUrl = rawBaseUrl.replace(/\/+$/, "");
    const wsUrl = `${wsBaseUrl}/ws/events/`;

    console.log("[WS] Intentando conectar a:", wsUrl);

    const socket = new WebSocket(wsUrl);

    socket.onopen = () => {
      console.log("[WS] Conectado");
    };

    socket.onmessage = (event: MessageEvent) => {
      try {
        const data: EventoFSM = JSON.parse(event.data);
        console.log("[WS] Mensaje recibido:", data);

        if (!data || !data.evento) {
          console.warn("[WS] Payload inválido:", data);
          return;
        }

        onEventoRecibidoRef.current(data);
      } catch (error) {
        console.error("[WS] Error parseando mensaje:", error, event.data);
      }
    };

    socket.onerror = (error) => {
      console.error("[WS] Error:", error);
    };

    socket.onclose = (event: CloseEvent) => {
      console.warn("[WS] Cerrado", {
        code: event.code,
        reason: event.reason,
        wasClean: event.wasClean,
      });
    };

    return () => {
      console.log("[WS] Cleanup. Estado actual:", socket.readyState);

      if (
        socket.readyState === WebSocket.OPEN ||
        socket.readyState === WebSocket.CONNECTING
      ) {
        socket.close();
      }
    };
  }, []);

  return null;
};

export default EventoListener;