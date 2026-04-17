import { useState } from "react";
import axios from "axios";

export default function History() {
  const [email, setEmail] = useState("");
  const [history, setHistory] = useState([]);

  const loadHistory = async () => {
    try {
      const res = await axios.get(
        `http://localhost:5000/api/history/${email}`
      );
      setHistory(res.data);
    } catch (err) {
      console.log(err);
      alert("Error loading history");
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>📊 Analysis History</h1>

      <input
        placeholder="Enter email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />

      <button onClick={loadHistory}>Load History</button>

      <div style={{ marginTop: 20 }}>
        {history.map((h, i) => (
          <div key={i} style={styles.card}>
            <p>📧 Email: {h[1]}</p>
            <p>📈 Score: {h[2]}%</p>
            <p>✅ Matched: {h[3]}</p>
            <p>❌ Missing: {h[4]}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

const styles = {
  card: {
    padding: 10,
    marginBottom: 10,
    border: "1px solid #ddd",
    borderRadius: 10
  }
};