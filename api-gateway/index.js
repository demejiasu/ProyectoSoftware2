const express = require("express");
const axios = require("axios");
const app = express();

// CORS
app.use((req, res, next) => {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS");
  res.header("Access-Control-Allow-Headers", "Content-Type, Authorization");
  if (req.method === "OPTIONS") {
    return res.sendStatus(200);
  }
  next();
});

app.use(express.json());

// AUTH
app.post("/auth/login", async (req, res) => {
  try {
    console.log("Login request:", req.body);
    const r = await axios.post("http://auth-service:8000/login", req.body);
    res.json(r.data);
  } catch (e) {
    console.error("Login error:", e.message);
    res.status(500).json({ error: e.message });
  }
});

app.post("/auth/logout", async (req, res) => {
  try {
    const r = await axios.post("http://auth-service:8000/logout", req.body);
    res.json(r.data);
  } catch (e) {
    console.error("Logout error:", e.message);
    res.status(500).json({ error: e.message });
  }
});

app.post("/auth/recover", async (req, res) => {
  try {
    console.log("Recover request:", req.body);
    const r = await axios.post("http://auth-service:8000/recover", req.body);
    res.json(r.data);
  } catch (e) {
    console.error("Recover error:", e.message);
    res.status(500).json({ error: e.message });
  }
});

// USERS
app.get("/users", async (req, res) => {
  try {
    const r = await axios.get("http://user-service:8001/users");
    res.json(r.data);
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

// PRODUCTS
app.get("/products", async (req, res) => {
  try {
    const r = await axios.get("http://product-service:8002/products");
    res.json(r.data);
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

app.get("/orders", async (req, res) => {
  try {
    const r = await axios.get("http://order-service:8003/orders");
    res.json(r.data);
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

app.get("/notify", async (req, res) => {
  try {
    const r = await axios.get("http://notification-service:8004/notify");
    res.json(r.data);
  } catch (e) {
    res.status(500).json({ error: e.message });
  }
});

app.get("/", (req, res) => {
  res.send("API Gateway funcionando");
});

app.listen(3000, () => console.log("Gateway running on port 3000"));