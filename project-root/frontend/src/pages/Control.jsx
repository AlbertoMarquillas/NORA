import { useNavigate } from 'react-router-dom';
import '../styles/EstadoSistema.css'; // reutiliza el estilo oscuro

const Control = () => {
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
      <h2>Control General del Sistema</h2>
      <div className="actions-container">
        <button onClick={() => handleAction('encender')}>Encender Sistema</button>
        <button onClick={() => handleAction('apagar')}>Apagar Sistema</button>
        <button onClick={() => handleAction('reiniciar')}>Reiniciar Sistema</button>
        <button onClick={() => handleAction('reiniciarNora')}>Reiniciar NORA</button>
        <button onClick={() => handleAction('reposo')}>Modo Reposo</button>
        <button onClick={() => handleAction('cambiarEstadoAuto')}>Estado Automático</button>
      </div>
      <div style={{ textAlign: 'center', marginTop: '30px' }}>
        <button onClick={() => navigate('/debug/estado')}>← Volver al Panel Principal</button>
      </div>
    </div>
  );
};

export default Control;
