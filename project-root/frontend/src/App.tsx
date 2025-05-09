import { Suspense, useEffect, useState } from "react";
import { useRoutes, Routes, Route, Navigate } from "react-router-dom";
import Home from "./components/home";
import AdminDashboard from "./components/AdminDashboard";
import Profile from "./components/Profile";
import { useAuth } from "./context/AuthContext"; // Importa el contexto de autenticación
import { motion } from "framer-motion";
import { Avatar, AvatarFallback, AvatarImage } from "./components/ui/avatar";

// Mock authentication hook - replace with actual auth context/hook later
const useAuth = () => {
  // Mock implementation
  return {
    isAuthenticated: true, // Change to false to test guest view
    isGuest: false, // Change to true to test guest view
    isAdmin: true, // Change to false to test normal user view
    user: {
      name: "User",
      email: "user@example.com",
      avatar: null,
    },
    logout: () => console.log("Logout clicked"),
    login: () => console.log("Login clicked"),
    register: () => console.log("Register clicked"),
  };
};

function App() {
  const { isAdmin } = useAuth();

  return (
    <Suspense fallback={<p>Loading...</p>}>
      <>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route
            path="/admin"
            element={isAdmin ? <AdminDashboard /> : <Navigate to="/" />}
          />
          <Route path="/profile" element={<Profile />} />
          
          {import.meta.env.VITE_TEMPO === "true" && (
            <Route path="/tempobook/*" />
          )}
          
        </Routes>
        {import.meta.env.VITE_TEMPO === "true" && useRoutes(routes)}
      </>
    </Suspense>
  );
}

export default App;
