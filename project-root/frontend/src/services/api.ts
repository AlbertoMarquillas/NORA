import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000/api", // Asegúrate de usar tu backend real
  withCredentials: true,
});

export default api;
