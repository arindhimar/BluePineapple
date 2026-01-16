const data = require("../data/employeeData");

async function getAllEmployees(req, res) {
  res.json(await data.getAll());
}

async function getEmployee(req, res) {
  const emp = await data.getById(req.params.id);
  if (!emp) return res.status(404).json({ error: "Employee not found" });
  res.json(emp);
}

async function createEmployee(req, res) {
  const emp = await data.add(req.body);
  res.status(201).json(emp);
}

async function updateEmployee(req, res) {
  const emp = await data.update(req.params.id, req.body);
  if (!emp) return res.status(404).json({ error: "Employee not found" });
  res.json(emp);
}

async function deleteEmployee(req, res) {
  const ok = await data.remove(req.params.id);
  if (!ok) return res.status(404).json({ error: "Employee not found" });
  res.json({ message: "Deleted" });
}

async function bulkDeleteEmployees(req, res) {
  const { ids } = req.body;
  if (!Array.isArray(ids) || ids.length === 0) {
    return res.status(400).json({ error: "IDs array required" });
  }

  const removed = await data.removeMany(ids);
  res.json({ message: "Deleted", count: removed.length });
}

module.exports = {
  getAllEmployees,
  getEmployee,
  createEmployee,
  updateEmployee,
  deleteEmployee,
  bulkDeleteEmployees
};
