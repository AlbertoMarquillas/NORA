import React, { useEffect } from "react";
import api from "@/services/api"; // Asegúrate de que la ruta sea correcta

const TestCors = () => {
  useEffect(() => {
    api.get("/test-cors/")
      .then(res => {
        console.log("✅ Respuesta CORS OK:", res.data);
      })
      .catch(err => {
        console.error("❌ CORS error:", err);
      });
  }, []);

  return (
    <div style={{ padding: "2rem" }}>
      <h2>Probando conexión con el backend (CORS)</h2>
      <p>Abre la consola del navegador para ver el resultado.</p>
    </div>
  );
};

export default TestCors;
