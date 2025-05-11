import { Suspense } from "react";
import { Routes, Route, Navigate, useRoutes } from "react-router-dom";
import Home from "./components/home";
import AdminDashboard from "./components/AdminDashboard";
import Login from "./components/Login";
import Register from "./components/Register";
import Profile from "./components/Profile";
import NoraInteractionPage from "./components/NoraInteractionPage";
import routes from "tempo-routes";
import { useAuth } from "./context/AuthContext";
import PrivateRoute from "./routes/PrivateRoute";
import AdminRoute from "./routes/AdminRoute";
import GuestRedirect from "./routes/GuestRedirect";
import ConnectionStatusBar from "./components/ConnectionStatusBar";

function App() {
  const { isAdmin, isAuthenticated, isGuest, login, register, loading } = useAuth();

  if (loading) return <p className="text-white text-center mt-20">Cargando...</p>;

  return (
    <Suspense fallback={<p>Loading...</p>}>
      <>
        <Routes>
          <Route path="/" element={<Home />} />

          <Route
            path="/login"
            element={
              <GuestRedirect>
                <Login onLogin={login} />
              </GuestRedirect>
            }
          />

          <Route
            path="/register"
            element={
              <GuestRedirect>
                <Register onRegister={register} />
              </GuestRedirect>
            }
          />

          <Route
            path="/profile"
            element={
              <PrivateRoute>
                <Profile />
              </PrivateRoute>
            }
          />

          <Route
            path="/interaction"
            element={
              <PrivateRoute>
                <NoraInteractionPage />
              </PrivateRoute>
            }
          />

          <Route
            path="/admin"
            element={
              <AdminRoute>
                <AdminDashboard />
              </AdminRoute>
            }
          />

          {import.meta.env.VITE_TEMPO === "true" && (
            <Route path="/tempobook/*" />
          )}
        </Routes>
        <ConnectionStatusBar />
        {import.meta.env.VITE_TEMPO === "true" && useRoutes(routes)}
      </>
    </Suspense>
  );
}

export default App;
