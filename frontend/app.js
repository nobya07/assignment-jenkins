const express = require("express");
const axios = require("axios");

const app = express();
app.use(express.json());
app.use(express.static(__dirname));

app.post("/add", async (req, res) => {
  await axios.post("http://backend:5000/add", req.body);
  res.send("Data Sent to Backend");
});

app.get("/get", async (req, res) => {
  const response = await axios.get("http://backend:5000/get");
  res.json(response.data);
});

app.listen(3000, () => console.log("Frontend running"));
