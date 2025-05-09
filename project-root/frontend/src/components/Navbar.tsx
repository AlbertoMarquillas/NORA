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
import { Link } from "react-router-dom";


// Mock authentication state - replace with actual auth context/hook later
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

const Navbar = () => {
  const { isAuthenticated, isGuest, isAdmin, user, logout, login, register } =
    useAuth();
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  return (
    <motion.nav
      className="fixed top-0 left-0 right-0 z-50 bg-[#121212] shadow-lg py-4 px-6"
      initial={{ opacity: 0, y: -20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
    >
      <div className="flex justify-between items-center">
        {/* Brand Logo/Name */}
        <Link to="/">
          <motion.div
            className="text-2xl font-bold text-white cursor-pointer"
            whileHover={{ scale: 1.05 }}
          >
            <span className="text-cyan-400">NORA</span>
          </motion.div>
        </Link>


        {/* Desktop Navigation */}
        <div className="hidden md:flex items-center space-x-6">
          {isAuthenticated && (
            <>
              <NavLink href="/chat">Chat</NavLink>
              {!isGuest && <NavLink href="/profile">Profile</NavLink>}
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
                  <a href="/admin">Admin Dashboard</a>
                </DropdownMenuItem>
                <DropdownMenuItem className="text-white hover:bg-gray-800 hover:text-cyan-400 cursor-pointer">
                  System Status
                </DropdownMenuItem>
                <DropdownMenuItem className="text-white hover:bg-gray-800 hover:text-cyan-400 cursor-pointer">
                  Logs
                </DropdownMenuItem>
                <DropdownMenuItem className="text-white hover:bg-gray-800 hover:text-cyan-400 cursor-pointer">
                  Monitoring
                </DropdownMenuItem>
              </DropdownMenuContent>
            </DropdownMenu>
          )}

          {isAuthenticated ? (
            <motion.div whileHover={{ scale: 1.05 }} className="ml-2">
              <a href="/profile" className="block">
                <Avatar className="h-9 w-9 border-2 border-cyan-500/30 hover:border-cyan-400 transition-colors duration-200">
                  <AvatarImage src={user.avatar || undefined} />
                  <AvatarFallback className="bg-cyan-900/30 text-cyan-100">
                    <User className="h-5 w-5" />
                  </AvatarFallback>
                </Avatar>
              </a>
            </motion.div>
          ) : (
            <div className="flex items-center space-x-3">
              <Button
                variant="ghost"
                className="text-white hover:text-cyan-400 hover:bg-transparent hover:scale-105 transition-all duration-200"
                onClick={login}
              >
                <LogIn className="mr-2 h-4 w-4" /> Login
              </Button>
              <Button
                className="bg-blue-600 hover:bg-blue-700 text-white rounded-full px-4 py-2 hover:scale-105 transition-all duration-200"
                onClick={register}
              >
                <UserPlus className="mr-2 h-4 w-4" /> Register
              </Button>
            </div>
          )}
        </div>

        {/* Mobile Menu Button */}
        <button
          className="md:hidden text-white"
          onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
        >
          <svg
            className="w-6 h-6"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
          >
            {isMobileMenuOpen ? (
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M6 18L18 6M6 6l12 12"
              />
            ) : (
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M4 6h16M4 12h16M4 18h16"
              />
            )}
          </svg>
        </button>
      </div>

      {/* Mobile Menu */}
      {isMobileMenuOpen && (
        <motion.div
          className="md:hidden mt-4 py-2 space-y-2 bg-[#1a1a1a] rounded-md shadow-lg"
          initial={{ opacity: 0, height: 0 }}
          animate={{ opacity: 1, height: "auto" }}
          transition={{ duration: 0.3 }}
        >
          {isAuthenticated ? (
            <>
              <div className="flex items-center px-4 py-3 border-b border-gray-800">
                <Avatar className="h-10 w-10 border-2 border-cyan-500/30 mr-3">
                  <AvatarImage src={user.avatar || undefined} />
                  <AvatarFallback className="bg-cyan-900/30 text-cyan-100">
                    <User className="h-5 w-5" />
                  </AvatarFallback>
                </Avatar>
                <div>
                  <div className="text-white font-medium">{user.name}</div>
                  {user.email && (
                    <div className="text-gray-400 text-sm">{user.email}</div>
                  )}
                </div>
              </div>
              <MobileNavLink href="/chat">Chat</MobileNavLink>
              {!isGuest && (
                <MobileNavLink href="/profile">Profile</MobileNavLink>
              )}
            </>
          ) : (
            <>
              <button
                className="w-full text-left px-4 py-3 text-white hover:bg-gray-800 hover:text-cyan-400 flex items-center"
                onClick={login}
              >
                <LogIn className="mr-2 h-4 w-4" /> Login
              </button>
              <button
                className="w-full text-left px-4 py-3 text-white bg-blue-600/20 hover:bg-blue-600/40 hover:text-cyan-400 flex items-center"
                onClick={register}
              >
                <UserPlus className="mr-2 h-4 w-4" /> Register
              </button>
            </>
          )}

          {isAdmin && (
            <div className="py-2 border-t border-gray-800">
              <div className="text-white px-4 py-2 font-medium text-sm">
                DEBUG MENU
              </div>
              <div className="pl-6 space-y-1">
                <MobileNavLink href="/admin">Admin Dashboard</MobileNavLink>
                <MobileNavLink href="/debug/status">
                  System Status
                </MobileNavLink>
                <MobileNavLink href="/debug/logs">Logs</MobileNavLink>
                <MobileNavLink href="/debug/monitoring">
                  Monitoring
                </MobileNavLink>
              </div>
            </div>
          )}
        </motion.div>
      )}
    </motion.nav>
  );
};

// Helper components for navigation links
const NavLink = ({
  href,
  children,
}: {
  href: string;
  children: React.ReactNode;
}) => (
  <motion.a
    href={href}
    className="text-white hover:text-cyan-400 transition-colors duration-200"
    whileHover={{ scale: 1.05 }}
  >
    {children}
  </motion.a>
);

const MobileNavLink = ({
  href,
  children,
}: {
  href: string;
  children: React.ReactNode;
}) => (
  <a
    href={href}
    className="block px-4 py-2 text-white hover:bg-gray-800 hover:text-cyan-400 transition-all duration-200"
  >
    {children}
  </a>
);

export default Navbar;
