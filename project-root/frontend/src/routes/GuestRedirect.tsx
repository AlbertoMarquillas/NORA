import { Navigate } from "react-router-dom";
import { useAuth } from "@/context/AuthContext";
import Loader from "@/components/Loader";

const GuestRedirect = ({ children }: { children: JSX.Element }) => {
  const { isGuest, loading } = useAuth();

  if (loading) return <Loader />;

  return isGuest ? children : <Navigate to="/" replace />;
};

export default GuestRedirect;
