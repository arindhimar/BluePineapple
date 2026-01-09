const express = require("express");

const app = express();
const PORT = 3000;

app.use(express.json());

app.use((req, res, next) => {
  console.log(`${req.method} ${req.url}`);
  next();
});

app.get("/", (req, res) => {
  res.status(200).send("Welcome to Express!");
});

app.post("/data", (req, res) => {
  console.log(req.body);
  res.status(200).json({
    message: "Data received."
  });
});

app.get("/users", (req, res) => {
  const users = [
    { id: 1, name: "Arin" },
    { id: 2, name: "Ashish" },
    { id: 3, name: "Alvf" }
  ];

  res.status(200).json(users);
});

app.get("/external-posts", async (req, res, next) => {
  try {
    const response = await fetch("https://jsonplaceholder.typicode.com/posts");
    const data = await response.json();
    res.status(200).json(data);
  } catch (error) {
    next(error);
  }
});

app.use((req, res) => {
  res.status(404).json({
    error: "Route not found"
  });
});

app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({
    error: "Something went wrong!"
  });
});

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
