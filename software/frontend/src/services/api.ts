// src/services/api.ts
import axios from "axios";

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL, // asegúrate de tenerlo en el .env
});

export default api;
