import React, { createContext, useContext, useState, useEffect, ReactNode } from "react";
import api from "../lib/api"; // Axios instance with baseURL

const API_URL = import.meta.env.VITE_API_URL;

// User typing
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
  login: (email: string, password: string) => Promise<void>;
  logout: () => Promise<void>;
  fetchUser: () => Promise<void>;
  register: (username: string, email: string, password: string, password2: string) => Promise<void>;
  loading: boolean;
}


const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider = ({ children }: { children: ReactNode }) => {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchUser().finally(() => setLoading(false));
  }, []);

  const fetchUser = async () => {
    try {
      const response = await api.get("/auth/me", { withCredentials: true });
      const data = response.data;
      const user: User = {
        name: data.username,
        email: data.email,
        avatar: data.avatar ?? null,
        role: data.is_admin ? "admin" : data.is_guest ? "guest" : "user",
      };
      setUser(user);
    } catch (error: any) {
      if (error.response?.status === 401) {
        // No está logueado: comportamiento esperado
        console.info("Usuario no autenticado.");
      } else {
        console.error("Error inesperado al obtener usuario:", error);
      }
      setUser(null);
    }
  };

  const login = async (name: string, password: string) => {
  try {
    const response = await api.post("/auth/login/", {
      username: name,
      password,
    });

    const data = response.data;
    const user: User = {
      name: data.username,
      email: data.email,
      avatar: data.avatar ?? null,
      role: data.is_admin ? "admin" : data.is_guest ? "guest" : "user",
    };

    setUser(user);
    localStorage.setItem("accessToken", data.access);
    localStorage.setItem("refreshToken", data.refresh);
    console.log("Login response:", response.data);

    await fetchUser();
  } catch (error: any) {
    console.error("Login failed:", error.response?.data || error.message);
    throw error; // deja que el componente (ej. `Login.tsx`) maneje el error
  }
};


  const logout = async () => {
    try {
      const refresh = localStorage.getItem("refreshToken");
      await api.post("/auth/logout/", { refresh });
    } catch (err) {
      console.error("Logout error:", err);
    } finally {
      setUser(null);
      localStorage.removeItem("refreshToken");
      localStorage.removeItem("accessToken");
    }
  };

  const isAuthenticated = !!user && user.role !== "guest";
  const isAdmin = user?.role === "admin";
  const isGuest = user?.role === "guest" || !user;

 

const register = async (username: string, email: string, password: string, password2: string) => {
  try {
    await api.post("/auth/register/", {
      username,
      email,
      password,
      password2,
    });
  } catch (err: any) {
    console.error("Register error:", err.response?.data || err.message);
    throw new Error(
      err.response?.data?.detail ||
      "Error al registrar. Intenta con otro usuario o email."
    );
  }
};


 return (
    <AuthContext.Provider
      value={{
        user,
        isAuthenticated,
        isAdmin,
        isGuest,
        login,
        logout,
        fetchUser,
        register,
        loading,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error("useAuth must be used within an AuthProvider");
  }
  return context;
};
