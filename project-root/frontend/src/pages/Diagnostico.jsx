import { useNavigate } from 'react-router-dom';
import '../styles/EstadoSistema.css';

const Diagnostico = () => {
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
      <h2>Diagnóstico y Verificación</h2>
      <div className="actions-container">
        <button onClick={() => handleAction('verificarRed')}>Verificar Conexión de Red</button>
        <button onClick={() => handleAction('verificarWifi')}>Verificar Módulo WiFi</button>
        <button onClick={() => handleAction('verificarAlmacenamiento')}>Verificar Almacenamiento Externo</button>
        <button onClick={() => handleAction('verificarRTC')}>Verificar RTC</button>
        <button onClick={() => handleAction('verificarSensores')}>Verificar Sensores</button>
      </div>
      <div style={{ textAlign: 'center', marginTop: '30px' }}>
        <button onClick={() => navigate('/debug/estado')}>← Volver al Panel Principal</button>
      </div>
    </div>
  );
};

export default Diagnostico;
