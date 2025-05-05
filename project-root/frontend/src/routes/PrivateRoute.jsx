import { Navigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

const PrivateRoute = ({ children }) => {
  const { user } = useAuth();
  if (!user) {
    return <Navigate to="/login" replace />; // Redirige si no hay usuario logueado
  }
  return children; // Si el usuario está logueado, renderiza los hijos
};

export default PrivateRoute;
