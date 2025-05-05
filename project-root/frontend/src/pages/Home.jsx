import { Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import '../styles/Home.css';

const Home = () => {
  const { user } = useAuth();

  return (
    <div className="home-container">
      <header className="home-header">
        <h1>Bienvenido a NORA</h1>
        <p>Tu asistente físico inteligente para el día a día.</p>
      </header>

      <section className="home-content">
        <h2>¿Qué puede hacer NORA?</h2>
        <ul className="home-features-list">
          <li>Detectar tu presencia y atenderte sin tocar nada</li>
          <li>Gestionar tu agenda, tareas y hábitos</li>
          <li>Responder por voz o gestos</li>
          <li>Adaptarse a tu comportamiento con inteligencia contextual</li>
        </ul>
      </section>

      {!user && (
        <section className="home-actions">
          <Link to="/login">
            <button>Iniciar sesión</button>
          </Link>
          <Link to="/register">
            <button>Registrarse</button>
          </Link>
        </section>
      )}
    </div>
  );
};

export default Home;
