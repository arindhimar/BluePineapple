const fs = require('fs');
const path = require('path');
const Employee = require('../model/employeeModel');

const CSV_PATH = path.join(__dirname, '..', 'api', 'employees.csv');

function ensureFile() {
  if (!fs.existsSync(CSV_PATH)) fs.writeFileSync(CSV_PATH, '');
}

function readAllSync() {
  ensureFile();
  const raw = fs.readFileSync(CSV_PATH, 'utf8').trim();
  if (!raw) return [];
  const lines = raw.split(/\r?\n/).filter(Boolean);
  return lines.map((l) => Employee.fromCSVLine(l));
}

function writeAllSync(employees) {
  const data = employees.map((e) => e.toCSVLine()).join('\n') + '\n';
  fs.writeFileSync(CSV_PATH, data, 'utf8');
}

function getAll() {
  return readAllSync();
}

function getById(id) {
  const all = readAllSync();
  return all.find((e) => e.id === String(id)) || null;
}

function add(employeePayload) {
  const { valid, errors } = Employee.validate(employeePayload);
  if (!valid) return { error: errors };
  const emp = new Employee(employeePayload);
  const existing = getById(emp.id);
  if (existing) return { error: ['id already exists'] };
  const all = readAllSync();
  all.push(emp);
  writeAllSync(all);
  return emp;
}

function update(id, payload) {
  const all = readAllSync();
  const idx = all.findIndex((e) => e.id === String(id));
  if (idx === -1) return { error: ['not found'] };
  const updated = Object.assign({}, all[idx], payload);
  const { valid, errors } = Employee.validate(updated);
  if (!valid) return { error: errors };
  all[idx] = new Employee(updated);
  writeAllSync(all);
  return all[idx];
}

function remove(id) {
  const all = readAllSync();
  const idx = all.findIndex((e) => e.id === String(id));
  if (idx === -1) return { error: ['not found'] };
  const removed = all.splice(idx, 1)[0];
  writeAllSync(all);
  return removed;
}

module.exports = { getAll, getById, add, update, remove };
