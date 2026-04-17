import { BrowserRouter, Routes, Route } from "react-router-dom";
import App from "./App";
import History from "./History";
import Login from "./Login";

export default function Main() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<App />} />
        <Route path="/history" element={<History />} />
        <Route path="/login" element={<Login />} />
      </Routes>
    </BrowserRouter>
  );
}