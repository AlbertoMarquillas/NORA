import { useAuth } from "@/context/AuthContext";
import { Navigate } from "react-router-dom";
import Loader from "@/components/Loader";

const PrivateRoute = ({ children }: { children: JSX.Element }) => {
  const { isAuthenticated, loading } = useAuth();

  if (loading) return <Loader />;
  return isAuthenticated ? children : <Navigate to="/login" replace />;
};

export default PrivateRoute;
