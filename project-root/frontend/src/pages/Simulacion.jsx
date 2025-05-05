import { useNavigate } from 'react-router-dom';
import '../styles/EstadoSistema.css';

const Simulacion = () => {
  const navigate = useNavigate();

  const enviarEventoFSM = async (evento, descripcion) => {
    const payload = {
      type: 'fsm_event',
      evento,
      descripcion,
    };

    try {
      const res = await fetch('http://localhost:8000/api/evento/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      });

      if (!res.ok) {
        console.error(`Error al enviar evento FSM: ${evento}.`);
      }
    } catch (err) {
      console.error('Error de conexión con backend:', err);
    }
  };

  // Definición por columnas
  const columnas = [
    {
      titulo: 'Activación',
      eventos: [
        { nombre: 'EVT_NFC_ACTIVATE', desc: 'Activación por NFC' },
        { nombre: 'EVT_WAKEWORD', desc: 'Activación por palabra clave' },
        { nombre: 'EVT_PRESENCE_CONFIRMED', desc: 'Presencia confirmada' },
        { nombre: 'EVT_ATTENTION_GAINED', desc: 'Atención visual sostenida' },
        { nombre: 'EVT_SCHEDULE_TRIGGERED', desc: 'Activación por agenda' },
      ],
    },
    {
      titulo: 'Interacción',
      eventos: [
        { nombre: 'EVT_SPEECH_START', desc: 'Inicio de entrada de voz' },
        { nombre: 'EVT_ATTENTION_CONFIRMED', desc: 'Atención visual mantenida' },
        { nombre: 'EVT_SPEECH_RECOGNIZED', desc: 'Entrada verbal reconocida' },
        { nombre: 'EVT_GESTURE_COMMAND', desc: 'Comando gestual interpretado' },
      ],
    },
    {
      titulo: 'Suspensión',
      eventos: [
        { nombre: 'EVT_IDLE_TIMEOUT', desc: 'Tiempo de inactividad excedido' },
        { nombre: 'EVT_ATTENTION_LOST', desc: 'Atención visual perdida' },
      ],
    },
    {
      titulo: 'Expiración',
      eventos: [
        { nombre: 'EVT_LISTEN_TIMEOUT', desc: 'Timeout durante ESCUCHA' },
      ],
    },
    {
      titulo: 'Error',
      eventos: [
        { nombre: 'EVT_MODULE_FAILURE', desc: 'Falla técnica en módulo' },
        { nombre: 'EVT_MIC_FAILURE', desc: 'Falla en el micrófono' },
        { nombre: 'EVT_PROCESS_FAILURE', desc: 'Error en el procesamiento' },
      ],
    },
    {
      titulo: 'Finalización',
      eventos: [
        { nombre: 'EVT_PROCESS_COMPLETED', desc: 'Proceso completado' },
        { nombre: 'EVT_RECOVERY_SUCCESS', desc: 'Recuperación automática' },
        { nombre: 'T_ERROR_RECOVERY_TIMEOUT', desc: 'Timeout recuperación' },
      ],
    },
    {
      titulo: 'Comandos',
      eventos: [
        { nombre: 'CMD_FORCE_RESUME', desc: 'Forzar reanudación' },
        { nombre: 'CMD_INHIBIR_ACTIVACION', desc: 'Inhibir activación' },
        { nombre: 'CMD_INHIBIR_ESCUCHA', desc: 'Inhibir escucha' },
        { nombre: 'CMD_CANCEL_LISTENING', desc: 'Cancelar escucha' },
      ],
    },
    {
        titulo: 'Acciones físicas',
        eventos: [
          { nombre: 'EVT_NFC_ACTIVATE', desc: 'Acerco tarjeta NFC válida' },
          { nombre: 'EVT_WAKEWORD', desc: 'Digo la hotword (palabra clave)' },
          { nombre: 'EVT_SPEECH_START', desc: 'Empiezo a hablar' },
          { nombre: 'EVT_LISTEN_TIMEOUT', desc: 'Paro de hablar sin respuesta' },
          { nombre: 'EVT_ATTENTION_GAINED', desc: 'Miro fijamente a NORA' },
          { nombre: 'EVT_ATTENTION_LOST', desc: 'Dejo de mirar a NORA' },
          { nombre: 'EVT_PRESENCE_CONFIRMED', desc: 'Paso cerca del sensor' },
          { nombre: 'EVT_IDLE_TIMEOUT', desc: 'Me ausento un buen rato' },
        ],
      }      
  ];

  return (
    <div className="estado-container">
      <h2>Simulación de Eventos FSM</h2>
      <div className="fsm-grid">
        {columnas.map((col, idx) => (
          <div key={idx} className="fsm-column">
            <h3>{col.titulo}</h3>
            {col.eventos.map((ev, i) => (
              <button key={i} onClick={() => enviarEventoFSM(ev.nombre, ev.desc)}>
                {ev.nombre}
              </button>
            ))}
          </div>
        ))}
      </div>
      <div className="volver-panel">
        <button onClick={() => navigate('/debug/estado')}>← Volver al Panel Principal</button>
        </div>

    </div>
  );
};

export default Simulacion;
