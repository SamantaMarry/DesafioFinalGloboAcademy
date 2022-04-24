
import axios from "axios";
const api = axios.create({
  baseURL: "http://192.168.0.180:5000/",
  // baseURL: "http://127.0.0.1:5000/",
  // baseURL: "http://localhost:3334/",
});
export default api;