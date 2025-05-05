import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import '../styles/Login.css';

const Login = () => {
  const [emailOrUsername, setEmailOrUsername] = useState('');
  const [password, setPassword] = useState('');
  const [guestName, setGuestName] = useState('');
  const { login } = useAuth();
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Realizar la llamada a la API de login
    const response = await fetch('http://localhost:8000/api/auth/login/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username_or_email: emailOrUsername, password }),
    });

      const data = await response.json();
    
      if (response.ok) {
        // Si el login es exitoso, guarda los datos del usuario
        const userData = {
          username: data.username,
          isAdmin: data.is_admin,         // Recibimos is_admin del backend
          isGuest: data.is_guest,         // Recibimos is_guest del backend
          isNoraAdmin: data.is_nora_admin, // Recibimos is_nora_admin del backend
          token: data.access,             // Guarda el token para futuras peticiones
        };
    
        // Guarda los datos en el contexto
        login(userData);
        
        // Redirige a la página de perfil
        navigate('/perfil');
      } else {
        // Manejo de errores si el login falla
        alert('Credenciales incorrectas');
      }
    };
    

    const handleGuest = () => {
      if (!guestName.trim()) return;

    // Login como invitado
    const userData = { username: guestName.trim(), isAdmin: false, isGuest: true };
    login(userData);
    navigate('/chat');  // Ruta exclusiva para invitados
  };

  return (
    <div className="auth-container">
      <h2>Iniciar sesión</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Correo electrónico o nombre de usuario"
          value={emailOrUsername}
          onChange={(e) => setEmailOrUsername(e.target.value)}
          required
        />
        <input
          type="password"
          placeholder="Contraseña"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <button type="submit">Entrar</button>
      </form>

      <div className="guest-login">
        <p>O entrar como invitado:</p>
        <input
          type="text"
          placeholder="Nombre"
          value={guestName}
          onChange={(e) => setGuestName(e.target.value)}
        />
        <button onClick={handleGuest}>Entrar como invitado</button>
      </div>
    </div>
  );
};

export default Login;
