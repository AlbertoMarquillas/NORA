import { Route, Routes } from "react-router-dom";
import Home from "@/views/Home";
import Profile from "@/views/Profile";
import Login from "@/views/Login";
import AdminDashboard from "@/views/AdminDashboard";
import ProtectedRoute from "@/router/ProtectedRoute";
import NotFound from "@/views/NotFound";
import path from 'path';
import Register from "@/views/Register";
import TestCors from "@/views/TestCors";
import NoraInteractionPage from "../views/NoraInteractionPage";

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
      <Route path="/test-cors" element={<TestCors />} />
      <Route
        path="/interaction"
        element={
          <ProtectedRoute allowedRoles={["admin"]}>
            <NoraInteractionPage />
          </ProtectedRoute>
        }
      />
      <Route path="*" element={<NotFound />} />

    </Routes>
  );
};

export default AppRoutes;
