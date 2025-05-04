import { Link } from 'react-router-dom';
import '../styles/Navbar.css';

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="navbar-logo">
        <Link to="/">NORA</Link>
      </div>
      <div className="navbar-links">
        <Link to="/login">Iniciar sesión</Link>
        <Link to="/register">Registrarse</Link>
      </div>
    </nav>
  );
};

export default Navbar;
