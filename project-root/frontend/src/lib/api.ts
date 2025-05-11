import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000/api", // cambia a tu backend real
  withCredentials: true, // útil si usas cookies
  headers: {
    "Content-Type": "application/json",
  },
});

export default api;
