import React, { createContext, useContext, useState, useEffect, ReactNode } from "react";

// Tipado del usuario
interface User {
  name: string;
  email: string;
  avatar?: string | null;
  role: "admin" | "user" | "guest";
}

interface AuthContextType {
  user: User | null;
  isAuthenticated: boolean;
  isAdmin: boolean;
  isGuest: boolean;
  login: (user: User) => void;
  logout: () => void;
}

// Crear contexto
const AuthContext = createContext<AuthContextType | undefined>(undefined);

// Proveedor
export const AuthProvider = ({ children }: { children: ReactNode }) => {
  const [user, setUser] = useState<User | null>(null);

  useEffect(() => {
    // Aquí podrías cargar datos del usuario desde localStorage o backend si quieres persistencia
    // const savedUser = localStorage.getItem("nora-user");
    // if (savedUser) setUser(JSON.parse(savedUser));
  }, []);

  const login = (newUser: User) => {
    setUser(newUser);
    // localStorage.setItem("nora-user", JSON.stringify(newUser));
  };

  const logout = () => {
    setUser(null);
    // localStorage.removeItem("nora-user");
  };

  const isAuthenticated = !!user && user.role !== "guest";
  const isAdmin = user?.role === "admin";
  const isGuest = user?.role === "guest" || !user;

  return (
    <AuthContext.Provider
      value={{ user, isAuthenticated, isAdmin, isGuest, login, logout }}
    >
      {children}
    </AuthContext.Provider>
  );
};

// Hook personalizado para acceder fácilmente al contexto
export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error("useAuth must be used within an AuthProvider");
  }
  return context;
};
