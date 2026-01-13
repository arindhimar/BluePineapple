const data = require("../data/employeeData");

async function getAllEmployees(req, res) {
  const all = data.getAll();
  res.json(all);
}

async function getEmployee(req, res) {
  const { id } = req.params;
  const emp = data.getById(id);
  if (!emp) return res.status(404).json({ error: "Employee not found" });
  res.json(emp);
}

async function createEmployee(req, res) {
  const result = data.add(req.body);
  if (result && result.error)
    return res.status(400).json({ errors: result.error });
  res.status(201).json(result);
}

async function updateEmployee(req, res) {
  const { id } = req.params;
  const result = data.update(id, req.body);
  if (result && result.error)
    return res.status(404).json({ errors: result.error });
  res.json(result);
}

async function deleteEmployee(req, res) {
  const { id } = req.params;
  const result = data.remove(id);
  if (result && result.error)
    return res.status(404).json({ errors: result.error });
  res.json({ message: "Deleted", employee: result });
}

module.exports = {
  getAllEmployees,
  getEmployee,
  createEmployee,
  updateEmployee,
  deleteEmployee,
};
