import { createContext, useContext, useState, useEffect } from 'react';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);  // null = no logueado

  useEffect(() => {
    const storedUser = localStorage.getItem('nora-user');
    if (storedUser) {
      setUser(JSON.parse(storedUser));
    }
  }, []);

  const login = (userData) => {
    setUser(userData);
    localStorage.setItem('nora-user', JSON.stringify(userData));  // Guardamos todos los datos
  };

  const logout = () => {
    setUser(null);
    localStorage.removeItem('nora-user');
  };

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
