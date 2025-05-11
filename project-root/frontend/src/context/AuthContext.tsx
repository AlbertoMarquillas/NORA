import React, { createContext, useContext, useState, useEffect, ReactNode } from "react";
import api from "../lib/api"; // cliente axios con baseURL


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
  login: (email: string, password: string) => Promise<void>;
  logout: () => Promise<void>;
  fetchUser: () => Promise<void>;
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
      const response = await api.get("/auth/me");
      setUser(response.data);
    } catch (error) {
      setUser(null);
    }
  };

const login = async (email: string, password: string) => {
  const response = await api.post("/auth/login/", {
    username_or_email: email,
    password,
  });

  const data = response.data;
  const user: User = {
    name: data.username,
    email: data.email,
    avatar: data.avatar ?? null,
    role: data.is_admin ? "admin" : data.is_guest ? "guest" : "user",
  };

  console.log("Login result →", {
    is_admin: data.is_admin,
    is_guest: data.is_guest,
    username: data.username,
  });


  setUser(user);
  localStorage.setItem("accessToken", data.access);
  localStorage.setItem("refreshToken", data.refresh);
};




const logout = async () => {
  try {
    const refresh = localStorage.getItem("refreshToken"); // o donde lo guardes
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

  return (
    <AuthContext.Provider value={{ user, isAuthenticated, isAdmin, isGuest, login, logout, fetchUser }}>
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
