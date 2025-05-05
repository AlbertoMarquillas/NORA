import { useNavigate } from 'react-router-dom';
import '../styles/EstadoSistema.css';

const Modulos = () => {
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
      <h2>Control de Módulos Físicos</h2>
      <div className="actions-container">
        <button onClick={() => handleAction('activarCamara')}>Activar Cámara</button>
        <button onClick={() => handleAction('desactivarCamara')}>Desactivar Cámara</button>

        <button onClick={() => handleAction('activarMicrofono')}>Activar Micrófono</button>
        <button onClick={() => handleAction('desactivarMicrofono')}>Desactivar Micrófono</button>

        <button onClick={() => handleAction('activarAltavoz')}>Activar Altavoz</button>
        <button onClick={() => handleAction('desactivarAltavoz')}>Desactivar Altavoz</button>

        <button onClick={() => handleAction('activarPantalla')}>Activar Pantalla</button>
        <button onClick={() => handleAction('desactivarPantalla')}>Desactivar Pantalla</button>

        <button onClick={() => handleAction('activarLeds')}>Activar LEDs RGB</button>
        <button onClick={() => handleAction('desactivarLeds')}>Desactivar LEDs RGB</button>

        <button onClick={() => handleAction('activarServos')}>Activar Servomotores</button>
        <button onClick={() => handleAction('desactivarServos')}>Desactivar Servomotores</button>

        <button onClick={() => handleAction('activarSensores')}>Activar Sensores</button>
        <button onClick={() => handleAction('desactivarSensores')}>Desactivar Sensores</button>

        <button onClick={() => handleAction('activarNFC')}>Activar NFC</button>
        <button onClick={() => handleAction('desactivarNFC')}>Desactivar NFC</button>

        <button onClick={() => handleAction('activarBluetooth')}>Activar Bluetooth</button>
        <button onClick={() => handleAction('desactivarBluetooth')}>Desactivar Bluetooth</button>
      </div>
      <div style={{ textAlign: 'center', marginTop: '30px' }}>
        <button onClick={() => navigate('/debug/estado')}>← Volver al Panel Principal</button>
      </div>
    </div>
  );
};

export default Modulos;
