import { Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Login from './pages/Login';
import Register from './pages/Register';
import Perfil from './pages/Perfil';
import PrivateRoute from './routes/PrivateRoute';
import Navbar from './components/Navbar';
import EstadoSistema from './pages/EstadoSistema';
import Logs from './pages/Logs';
import Monitoreo from './pages/Monitoreo';
import Control from './pages/Control';
import Modulos from './pages/Modulos';
import Diagnostico from './pages/Diagnostico';
import Simulacion from './pages/Simulacion';
import Agentes from './pages/Agentes';
import Admin from './pages/Admin';


function App() {
  return (
    <>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route
          path="/perfil"
          element={
            <PrivateRoute>
              <Perfil />
            </PrivateRoute>
          }
        />
        <Route path="/debug/estado" element={<EstadoSistema />} />
        <Route path="/debug/logs" element={<Logs />} />
        <Route path="/debug/monitoreo" element={<Monitoreo />} />
        <Route path="/debug/control" element={<Control />} />
        <Route path="/debug/modulos" element={<Modulos />} />
        <Route path="/debug/monitoreo" element={<Monitoreo />} />
        <Route path="/debug/diagnostico" element={<Diagnostico />} />
        <Route path="/debug/simulacion" element={<Simulacion />} />
        <Route path="/debug/agentes" element={<Agentes />} />
        <Route path="/debug/admin" element={<Admin />} />
      </Routes>
    </>
  );
}

export default App;
