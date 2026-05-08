const express = require("express");
const axios = require("axios");
const path = require("path");
const app = express();

// Servir archivos estáticos del frontend
app.use(express.static(path.join(__dirname, "public")));

// CORS
app.use((req, res, next) => {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS");
  res.header("Access-Control-Allow-Headers", "Content-Type, Authorization");
  if (req.method === "OPTIONS") return res.sendStatus(200);
  next();
});

app.use(express.json());

// ==================== AUTH ====================
app.post("/auth/login", async (req, res) => {
  try {
    const r = await axios.post("http://auth-service:8000/login", req.body);
    res.json(r.data);
  } catch (e) {
    res.status(e.response?.status || 500).json(e.response?.data || { error: e.message });
  }
});

app.post("/auth/register", async (req, res) => {
  try {
    const r = await axios.post("http://auth-service:8000/register", req.body);
    res.json(r.data);
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

app.get("/auth/verify", async (req, res) => {
  try {
    const r = await axios.get("http://auth-service:8000/verify", {
      headers: { Authorization: req.headers.authorization }
    });
    res.json(r.data);
  } catch (e) {
    res.status(401).json({ valid: false });
  }
});

// ==================== USERS ====================
app.get("/users", async (req, res) => {
  try {
    const r = await axios.get("http://user-service:8001/users");
    res.json(r.data);
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

app.post("/users", async (req, res) => {
  try {
    const r = await axios.post("http://user-service:8001/users", req.body);
    res.json(r.data);
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

app.put("/users/:id", async (req, res) => {
  try {
    const r = await axios.put(`http://user-service:8001/users/${req.params.id}`, req.body);
    res.json(r.data);
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

app.delete("/users/:id", async (req, res) => {
  try {
    const r = await axios.delete(`http://user-service:8001/users/${req.params.id}`);
    res.json(r.data);
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

// ==================== PRODUCTS ====================
app.get("/products", async (req, res) => {
  try {
    const r = await axios.get("http://product-service:8002/products");
    res.json(r.data);
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

app.post("/products", async (req, res) => {
  try {
    const r = await axios.post("http://product-service:8002/products", req.body);
    res.json(r.data);
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

app.put("/products/:id", async (req, res) => {
  try {
    const r = await axios.put(`http://product-service:8002/products/${req.params.id}`, req.body);
    res.json(r.data);
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

app.delete("/products/:id", async (req, res) => {
  try {
    const r = await axios.delete(`http://product-service:8002/products/${req.params.id}`);
    res.json(r.data);
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

// ==================== ORDERS ====================
app.get("/orders", async (req, res) => {
  try {
    const r = await axios.get("http://order-service:8003/orders");
    res.json(r.data);
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

app.post("/orders", async (req, res) => {
  try {
    const r = await axios.post("http://order-service:8003/orders", req.body);
    res.json(r.data);
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

app.put("/orders/:id", async (req, res) => {
  try {
    const r = await axios.put(`http://order-service:8003/orders/${req.params.id}`, req.body);
    res.json(r.data);
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

app.delete("/orders/:id", async (req, res) => {
  try {
    const r = await axios.delete(`http://order-service:8003/orders/${req.params.id}`);
    res.json(r.data);
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

// ==================== NOTIFICATIONS ====================
app.get("/notify", async (req, res) => {
  try {
    const r = await axios.get("http://notification-service:8004/notify");
    res.json(r.data);
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

app.post("/notify", async (req, res) => {
  try {
    const r = await axios.post("http://notification-service:8004/notify", req.body);
    res.json(r.data);
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

app.put("/notify/:id", async (req, res) => {
  try {
    const r = await axios.put(`http://notification-service:8004/notify/${req.params.id}`, req.body);
    res.json(r.data);
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

app.delete("/notify/:id", async (req, res) => {
  try {
    const r = await axios.delete(`http://notification-service:8004/notify/${req.params.id}`);
    res.json(r.data);
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

// Health check
app.get("/api/health", (req, res) => {
  res.json({ status: "ok", service: "API Gateway" });
});

// Redirigir todo al frontend
app.get("*", (req, res) => {
  res.sendFile(path.join(__dirname, "public", "index.html"));
});

app.listen(3000, () => console.log("Gateway running on port 3000"));