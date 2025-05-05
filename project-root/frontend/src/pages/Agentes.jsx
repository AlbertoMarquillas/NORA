import { useNavigate } from 'react-router-dom';
import '../styles/EstadoSistema.css';

const Agentes = () => {
  const navigate = useNavigate();

  const handleAction = async (action) => {
    try {
      const res = await fetch(`http://localhost:8000/api/debug/${action}/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
      });

      if (res.ok) {
        console.log(`Acción ${action} ejecutada correctamente.`);
      } else {
        console.error(`Error al ejecutar la acción ${action}.`);
      }
    } catch (err) {
      console.error('Error de conexión con el backend:', err);
    }
  };

  return (
    <div className="estado-container">
      <h2>Control de Agentes y Núcleo</h2>
      <div className="actions-container">
        <button onClick={() => handleAction('evaluarContexto')}>Forzar Evaluación de Contexto</button>
        <button onClick={() => handleAction('accionReflexiva')}>Forzar Acción Reflexiva</button>
        <button onClick={() => handleAction('resetEmocional')}>Reset Emocional del Sistema</button>
        <button onClick={() => handleAction('estadoAgenteCoordinador')}>Estado del Agente Coordinador</button>
        <button onClick={() => handleAction('estadoTodosAgentes')}>Estado de Todos los Agentes</button>
      </div>
      <div style={{ textAlign: 'center', marginTop: '30px' }}>
        <button onClick={() => navigate('/debug/estado')}>← Volver al Panel Principal</button>
      </div>
    </div>
  );
};

export default Agentes;
