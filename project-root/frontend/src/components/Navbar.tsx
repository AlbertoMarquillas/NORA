import React, { useState } from "react";
import { motion } from "framer-motion";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "./ui/dropdown-menu";
import { ChevronDown, LogOut, LogIn, User, UserPlus } from "lucide-react";
import { Button } from "./ui/button";
import { Avatar, AvatarFallback, AvatarImage } from "./ui/avatar";
import { Link, useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

import api from "../services/api"; // Asegúrate de tener esta instancia configurada

const Navbar = () => {
  const {
    isAuthenticated,
    isGuest,
    isAdmin,
    user,
    logout,
    login: contextLogin,
    register,
    loading,
  } = useAuth(); // <- aquí accedeixes també a loading

  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  const navigate = useNavigate();

  // 🔄 Si el context encara està carregant, evita renderitzar el Navbar
  if (loading) return null;

  const handleLogout = async () => {
    await logout();
    navigate("/");
  };

  const goToLogin = () => navigate("/login");
  const goToRegister = () => navigate("/register");

  return (
    <motion.nav
      className="fixed top-0 left-0 right-0 z-50 bg-[#121212] shadow-lg py-4 px-6"
      initial={{ opacity: 0, y: -20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
    >
      <div className="flex justify-between items-center">
        <Link to="/">
          <motion.div
            className="text-2xl font-bold text-white cursor-pointer"
            whileHover={{ scale: 1.05 }}
          >
            <span className="text-cyan-400">NORA</span>
          </motion.div>
        </Link>

        <div className="hidden md:flex items-center space-x-6">
          {isAuthenticated && (
            <>
              <NavLink href="/chat">Chat</NavLink>
            </>
          )}

          {isAdmin && (
            <DropdownMenu>
              <DropdownMenuTrigger asChild>
                <Button
                  className="flex items-center gap-1 px-3 py-1.5 rounded-md text-sm font-medium text-white border border-[#2f2f2f] bg-[#1a1a1a] hover:text-cyan-400 hover:border-cyan-500 hover:scale-105 transition-all duration-200"
                >
                  DEBUG <ChevronDown className="h-4 w-4" />
                </Button>
              </DropdownMenuTrigger>
              <DropdownMenuContent className="bg-[#1a1a1a] border-gray-700 shadow-lg">
                <DropdownMenuItem
                  className="text-white hover:bg-gray-800 hover:text-cyan-400 cursor-pointer"
                  asChild
                >
                  <Link to="/admin">Admin Dashboard</Link>
                </DropdownMenuItem>
                <DropdownMenuItem className="text-white hover:bg-gray-800 hover:text-cyan-400 cursor-pointer">
                  System Status
                </DropdownMenuItem>
                <DropdownMenuItem className="text-white hover:bg-gray-800 hover:text-cyan-400 cursor-pointer">
                  Logs
                </DropdownMenuItem>
                <DropdownMenuItem
                  className="text-white hover:bg-gray-800 hover:text-cyan-400 cursor-pointer"
                  asChild
                >
                  <Link to="/interaction">Interacción</Link>
                </DropdownMenuItem>
              </DropdownMenuContent>
            </DropdownMenu>
          )}

          {isAuthenticated ? (
            <motion.div whileHover={{ scale: 1.05 }} className="ml-2">
              <Link to="/profile">
                <Avatar className="h-9 w-9 border-2 border-cyan-500/30 hover:border-cyan-400 transition-colors duration-200">
                  <AvatarImage src={user.avatar || undefined} />
                  <AvatarFallback className="bg-cyan-900/30 text-cyan-100">
                    <User className="h-5 w-5" />
                  </AvatarFallback>
                </Avatar>
              </Link>
            </motion.div>


          ) : (
            <div className="flex items-center space-x-3">
              <Button
                variant="ghost"
                className="text-white hover:text-cyan-400 hover:bg-transparent hover:scale-105 transition-all duration-200"
                onClick={goToLogin}
              >
                <LogIn className="mr-2 h-4 w-4" /> Login
              </Button>
              <Button
                className="bg-blue-600 hover:bg-blue-700 text-white rounded-full px-4 py-2 hover:scale-105 transition-all duration-200"
                onClick={goToRegister}
              >
                <UserPlus className="mr-2 h-4 w-4" /> Register
              </Button>
            </div>
          )}
        </div>
      </div>
    </motion.nav>
  );
};

const NavLink = ({ href, children }: { href: string; children: React.ReactNode }) => (
  <motion.a
    href={href}
    className="text-white hover:text-cyan-400 transition-colors duration-200"
    whileHover={{ scale: 1.05 }}
  >
    {children}
  </motion.a>
);

export default Navbar;
