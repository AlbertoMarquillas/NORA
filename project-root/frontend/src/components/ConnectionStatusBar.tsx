import React, { useEffect, useState } from "react";
import { cn } from "@/lib/utils";

const API_URL = import.meta.env.VITE_API_URL;

const ConnectionStatusBar = () => {
  const [status, setStatus] = useState<"connected" | "disconnected" | "checking">("checking");

  useEffect(() => {
    const checkConnection = async () => {
      try {
        const res = await fetch(`${API_URL}/auth/me`, {
          headers: {
            Authorization: `Bearer ${localStorage.getItem("accessToken") || ""}`,
          },
        });

        if (res.ok) {
          setStatus("connected");
        } else {
          setStatus("disconnected");
        }
      } catch {
        setStatus("disconnected");
      }
    };

    checkConnection();               // Al iniciar
    const interval = setInterval(checkConnection, 5000); // Cada 5 segundos

    return () => clearInterval(interval);
  }, []);

  const text = {
    connected: `🟢 Conectado al backend (${API_URL})`,
    disconnected: `🔴 No se pudo conectar al backend (${API_URL})`,
    checking: `🟡 Verificando conexión... (${API_URL})`,
  };

  return (
    <div
      className={cn(
        "fixed bottom-0 left-0 right-0 text-sm text-white px-4 py-2 font-medium z-50 text-center",
        status === "connected" && "bg-green-600",
        status === "disconnected" && "bg-red-700",
        status === "checking" && "bg-yellow-700"
      )}
    >
      {text[status]}
    </div>
  );
};

export default ConnectionStatusBar;
