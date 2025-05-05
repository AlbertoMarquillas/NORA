import { useNavigate } from 'react-router-dom';
import '../styles/EstadoSistema.css';

const Admin = () => {
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
      <h2>Acciones del Administrador</h2>
      <div className="actions-container">
        <button onClick={() => handleAction('crearUsuario')}>Crear Usuario</button>
        <button onClick={() => handleAction('eliminarUsuario')}>Eliminar Usuario</button>
        <button onClick={() => handleAction('modificarUsuario')}>Modificar Usuario</button>
        <button onClick={() => handleAction('verConfiguracionAvanzada')}>Ver Configuración Avanzada</button>
        <button onClick={() => handleAction('descargarLogs')}>Descargar Logs del Sistema</button>
        <button onClick={() => handleAction('forzarActualizacion')}>Forzar Actualización de Software</button>
      </div>
      <div style={{ textAlign: 'center', marginTop: '30px' }}>
        <button onClick={() => navigate('/debug/estado')}>← Volver al Panel Principal</button>
      </div>
    </div>
  );
};

export default Admin;
