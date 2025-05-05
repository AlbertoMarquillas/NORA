import { useNavigate } from 'react-router-dom';
import '../styles/EstadoSistema.css';

const EstadoDelSistema = () => {
  const navigate = useNavigate();

  return (
    <div className="estado-container">
      <h2>Panel de Depuración del Sistema NORA</h2>
      <div className="actions-container">
        <button onClick={() => navigate('/debug/control')}>Control General del Sistema</button>
        <button onClick={() => navigate('/debug/modulos')}>Control de Módulos Físicos</button>
        <button onClick={() => navigate('/debug/monitoreo')}>Monitoreo en Tiempo Real</button>
        <button onClick={() => navigate('/debug/diagnostico')}>Diagnóstico y Verificación</button>
        <button onClick={() => navigate('/debug/simulacion')}>Simulación de Entradas</button>
        <button onClick={() => navigate('/debug/agentes')}>Control de Agentes y Núcleo</button>
        <button onClick={() => navigate('/debug/admin')}>Acciones del Administrador</button>
      </div>
    </div>
  );
};

export default EstadoDelSistema;
