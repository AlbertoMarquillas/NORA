import { Route, Routes } from "react-router-dom";
import Home from "@/views/Home";
import Profile from "@/views/Profile";
import Login from "@/views/Login";
import AdminDashboard from "@/views/AdminDashboard";
import ProtectedRoute from "@/router/ProtectedRoute";
import NotFound from "@/views/NotFound";
import Register from "@/views/Register"; // opcional
// import NotFound from "@/views/NotFound"; // opcional

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
      <Route
        path="/admin"
        element={
          <ProtectedRoute allowedRoles={["admin"]}>
            <AdminDashboard />
          </ProtectedRoute>
        }
      />
      <Route path="/login" element={<Login />} />
      
      {/* <Route path="*" element={<NotFound />} /> */}
      <Route path="/register" element={<Register />} /> {/* opcional */}
      {/* <Route path="/not-found" element={<NotFound />} /> opcional */}
      {/* <Route path="*" element={<Navigate to="/not-found" replace />} /> opcional */}

      {/* Catch-all route for 404 Not Found */}
      {/* <Route path="*" element={<NotFound />} /> opcional */}
      <Route path="*" element={<NotFound />} />

    </Routes>
  );
};

export default AppRoutes;
