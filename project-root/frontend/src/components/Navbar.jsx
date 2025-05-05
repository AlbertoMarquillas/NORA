import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import '../styles/Navbar.css';

const Navbar = () => {
  const { user, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/');
  };

  return (
    <nav className="navbar">
      <div className="navbar-left">
        <Link to="/" className="navbar-brand">NORA</Link>
      </div>

      <div className="navbar-right">
      {user && (
        <>
          {!user.isGuest && <Link to="/perfil">Perfil</Link>}  {/* Solo se muestra si no es invitado */}
          <Link to="/chat">Chat</Link>

          {user?.isAdmin && (
            <div className="dropdown">
              <button className="dropbtn">Debug</button>
              <div className="dropdown-content">
                <Link to="/debug/estado">Estado del sistema</Link>
                <Link to="/debug/logs">Logs</Link>
                <Link to="/debug/monitoreo">Monitoreo</Link>
              </div>
            </div>
          )}

          <button onClick={handleLogout}>Cerrar sesión</button>
        </>
      )}

      </div>
    </nav>
  );
};

export default Navbar;
