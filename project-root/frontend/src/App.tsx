import { Suspense } from "react";
import { useRoutes, Routes, Route, Navigate } from "react-router-dom";
import Home from "./components/home";
import AdminDashboard from "./components/AdminDashboard";
import Login from "./components/Login";
import Register from "./components/Register";
import Profile from "./components/Profile";
import NoraInteractionPage from "./components/NoraInteractionPage";
import routes from "tempo-routes";
import { useAuth } from "./context/AuthContext";
function App() {
  const { isAdmin, isAuthenticated, isGuest, login, register } = useAuth(); 

  return (
    <Suspense fallback={<p>Loading...</p>}>
      <>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login onLogin={login} />} />
          <Route
            path="/profile"
            element={isGuest ? <Navigate to="/" /> : <Profile />}
          />
          <Route path="/interaction" element={<NoraInteractionPage />} />
          <Route
            path="/register"
            element={<Register onRegister={register} />}
          />
          <Route
            path="/admin"
            element={isAdmin ? <AdminDashboard /> : <Navigate to="/" />}
          />
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
