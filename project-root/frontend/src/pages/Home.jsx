import { Link } from 'react-router-dom';
import '../styles/Home.css';

const Home = () => {
  return (
    <div className="home-container">
      <header className="home-header">
        <h1>Bienvenido a NORA</h1>
        <p>Tu asistente físico inteligente para el día a día.</p>
      </header>

      <section className="home-content">
        <h2>¿Qué puede hacer NORA?</h2>
        <ul>
          <li>Detectar tu presencia y atenderte sin tocar nada</li>
          <li>Gestionar tu agenda, tareas y hábitos</li>
          <li>Responder por voz o gestos</li>
          <li>Adaptarse a tu comportamiento con inteligencia contextual</li>
        </ul>
      </section>

      <section className="home-actions">
        <Link to="/login">
          <button>Iniciar sesión</button>
        </Link>
        <Link to="/register">
          <button>Registrarse</button>
        </Link>
      </section>
    </div>
  );
};

export default Home;
