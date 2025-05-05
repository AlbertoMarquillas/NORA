import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import '../styles/EstadoSistema.css';

const EstadoDelSistema = () => {
  const { user } = useAuth();
  const navigate = useNavigate();
  const [systemStatus, setSystemStatus] = useState('Activo'); // Simulando estado de sistema

  // Funciones para manejar las acciones
  const handleButtonClick = async (action) => {
    // Enviar solicitud al backend para activar/desactivar un módulo o cambiar estado
    const response = await fetch(`http://localhost:8000/api/debug/${action}/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
    });

    if (response.ok) {
      alert(`Acción ${action} ejecutada correctamente.`);
      setSystemStatus(action); // Actualiza el estado de sistema
    } else {
      alert('Error al ejecutar la acción.');
    }
  };

  return (
    <div className="estado-container">
      <h2>Estado del Sistema</h2>
      <div className="status-display">
        <h3>Estado Actual: {systemStatus}</h3>
      </div>

      <div className="actions-container">
        {/* Botones para simular las acciones de debug */}
        <h3>Control del Sistema</h3>
        <button onClick={() => handleButtonClick('encender')}>Encender Sistema</button>
        <button onClick={() => handleButtonClick('apagar')}>Apagar Sistema</button>
        <button onClick={() => handleButtonClick('reiniciar')}>Reiniciar Sistema</button>
        <button onClick={() => handleButtonClick('reposo')}>Modo Reposo</button>

        <h3>Control de Módulos</h3>
        <button onClick={() => handleButtonClick('activarModuloX')}>Activar Módulo X</button>
        <button onClick={() => handleButtonClick('desactivarModuloX')}>Desactivar Módulo X</button>

        <h3>Monitoreo del Sistema</h3>
        <button onClick={() => handleButtonClick('monitorearCPU')}>Monitorear CPU</button>
        <button onClick={() => handleButtonClick('verUsoMemoria')}>Ver Uso de Memoria</button>
        <button onClick={() => handleButtonClick('verLogs')}>Ver Logs</button>

        <h3>Diagnóstico</h3>
        <button onClick={() => handleButtonClick('verificarRed')}>Verificar Conexión a Red</button>
        <button onClick={() => handleButtonClick('verificarModuloRed')}>Verificar Módulo de Red</button>

        <h3>Reacciones Automáticas</h3>
        <button onClick={() => handleButtonClick('reiniciarNora')}>Reiniciar NORA</button>
        <button onClick={() => handleButtonClick('cambiarEstadoAuto')}>Cambiar Estado Automático</button>
      </div>

      {/* Mostrar los botones solo si el usuario es admin */}
      {user?.isAdmin && (
        <>
          <h3>Acciones de Administrador</h3>
          <button onClick={() => handleButtonClick('crearUsuario')}>Crear Usuario</button>
          <button onClick={() => handleButtonClick('eliminarUsuario')}>Eliminar Usuario</button>
          <button onClick={() => handleButtonClick('modificarUsuario')}>Modificar Usuario</button>
          <button onClick={() => handleButtonClick('verActividadUsuario')}>Ver Actividad de Usuario</button>
          <button onClick={() => handleButtonClick('verConfiguracionAvanzada')}>Ver Configuración Avanzada</button>
        </>
      )}
    </div>
  );
};

export default EstadoDelSistema;
