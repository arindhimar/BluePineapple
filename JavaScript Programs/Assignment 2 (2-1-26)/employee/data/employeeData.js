const fs = require('fs');
const path = require('path');

const CSV_PATH = path.join(__dirname, '../api/employees.csv');

function ensureFile() {
  const dir = path.dirname(CSV_PATH);

  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }

  if (!fs.existsSync(CSV_PATH)) {
    fs.writeFileSync(CSV_PATH, '', 'utf8');
  }
}

function readAllSync() {
  ensureFile();

  const data = fs.readFileSync(CSV_PATH, 'utf8');
  if (!data.trim()) return [];

  return data
    .trim()
    .split('\n')
    .map(line => {
      const [id, name, email, gender] = line.split(',');
      return {
        id: String(id),
        name: name || '',
        email: email || '',
        gender: gender || ''
      };
    });
}

function writeAllSync(employees) {
  ensureFile();

  const data = employees
    .map(e => `${e.id},${e.name},${e.email},${e.gender}`)
    .join('\n');

  fs.writeFileSync(CSV_PATH, data + '\n', 'utf8');
}

function getAll() {
  return readAllSync();
}

function getById(id) {
  return readAllSync().find(e => e.id === String(id)) || null;
}

function add(data) {
  const all = readAllSync();

  const emp = {
    id: String(data.id),
    name: data.name || '',
    email: data.email || '',
    gender: data.gender || ''
  };

  all.push(emp);
  writeAllSync(all);
  return emp;
}

function update(id, data) {
  const all = readAllSync();
  const index = all.findIndex(e => e.id === String(id));

  if (index === -1) return null;

  all[index] = { ...all[index], ...data, id: String(id) };
  writeAllSync(all);
  return all[index];
}

function remove(id) {
  const all = readAllSync();
  const index = all.findIndex(e => e.id === String(id));

  if (index === -1) return null;

  const removed = all.splice(index, 1)[0];
  writeAllSync(all);
  return removed;
}

module.exports = { getAll, getById, add, update, remove };
