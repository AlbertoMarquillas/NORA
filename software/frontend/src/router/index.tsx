import { Route, Routes } from "react-router-dom";
import Home from "@/views/Home";
import Profile from "@/views/Profile";
import Login from "@/views/Login";
import ProtectedRoute from "@/router/ProtectedRoute";

// Add other views as needed

const AppRoutes = () => {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route
        path="/profile"
        element={
          <ProtectedRoute allowedRoles={["admin", "user"]}>
            <Profile />
          </ProtectedRoute>
        }
      />
      <Route path="/login" element={<Login />} />
    </Routes>
  );
};

export default AppRoutes;
