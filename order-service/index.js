const express = require("express");
const app = express();

app.use(express.json());

let orders = [];
let nextId = 1;

app.get("/orders", (req, res) => {
  res.json({ orders });
});

app.post("/orders", (req, res) => {
  const { product, quantity, total } = req.body;
  const order = {
    id: nextId++,
    product: product || "",
    quantity: quantity || 1,
    total: total || 0,
    status: "pending",
    date: new Date().toISOString()
  };
  orders.push(order);
  res.status(201).json(order);
});

app.put("/orders/:id", (req, res) => {
  const id = parseInt(req.params.id);
  const order = orders.find(o => o.id === id);
  if (!order) return res.status(404).json({ error: "Order not found" });
  
  const { product, quantity, total, status } = req.body;
  if (product) order.product = product;
  if (quantity) order.quantity = quantity;
  if (total) order.total = total;
  if (status) order.status = status;
  
  res.json(order);
});

app.delete("/orders/:id", (req, res) => {
  const id = parseInt(req.params.id);
  const index = orders.findIndex(o => o.id === id);
  if (index === -1) return res.status(404).json({ error: "Order not found" });
  
  orders.splice(index, 1);
  res.json({ message: "Order deleted" });
});

app.listen(8003, () => {
  console.log("Order service running on port 8003");
});