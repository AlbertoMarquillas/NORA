import { Navigate } from "react-router-dom";
import { useAuth } from "@/context/AuthContext";
import Loader from "@/components/Loader";


const AdminRoute = ({ children }: { children: JSX.Element }) => {
  const { isAdmin, loading } = useAuth();

  if (loading) return <Loader />;

  return isAdmin ? children : <Navigate to="/" replace />;
  
};

export default AdminRoute;
