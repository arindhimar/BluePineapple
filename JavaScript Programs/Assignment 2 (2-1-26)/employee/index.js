const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;
const employeeRouter = require('./api/employeeRoutes');

app.use(express.json());
app.use('/api', employeeRouter);

app.get('/', (req, res) => {
  res.json({ message: 'Employee API is up. Use /api/employees' });
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
