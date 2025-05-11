import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000/api",
});

// Añadir token en cada petición
api.interceptors.request.use((config) => {
  const token = localStorage.getItem("accessToken");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Manejar expiración y refresh automático
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;

    if (
      error.response?.status === 401 &&
      !originalRequest._retry &&
      localStorage.getItem("refreshToken")
    ) {
      originalRequest._retry = true;
      try {
        const refresh = localStorage.getItem("refreshToken");
        const res = await axios.post("http://localhost:8000/api/auth/refresh/", { refresh });
        const newAccess = res.data.access;

        localStorage.setItem("accessToken", newAccess);
        api.defaults.headers.common["Authorization"] = `Bearer ${newAccess}`;
        originalRequest.headers["Authorization"] = `Bearer ${newAccess}`;

        return api(originalRequest);
      } catch (err) {
        console.error("No se pudo refrescar el token.");
        localStorage.removeItem("accessToken");
        localStorage.removeItem("refreshToken");
        return Promise.reject(err);
      }
    }

    return Promise.reject(error);
  }
);

export default api;
