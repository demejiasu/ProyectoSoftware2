const express = require("express");
const app = express();

app.get("/orders", (req, res) => {
  res.json({ orders: [] });
});

app.listen(8003, () => {
  console.log("Order service running on port 8003");
});