import axios from "axios";

const BASE_URL = "http://127.0.0.1:5000";

export const uploadResume = (formData) => {
  return axios.post(`${BASE_URL}/resume/upload`, formData);
};

export const analyzeResume = (data) => {
  return axios.post(`${BASE_URL}/analysis/analyze`, data);
};