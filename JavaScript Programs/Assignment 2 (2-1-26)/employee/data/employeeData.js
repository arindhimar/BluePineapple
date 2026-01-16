const fs = require("fs");
const path = require("path");

const CSV_PATH = path.join(__dirname, "../api/employees.csv");

/* ---------- Helpers ---------- */
function ensureFile() {
  const dir = path.dirname(CSV_PATH);
  if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
  if (!fs.existsSync(CSV_PATH)) fs.writeFileSync(CSV_PATH, "", "utf8");
}

async function readAll() {
  ensureFile();
  const content = await fs.promises.readFile(CSV_PATH, "utf8");
  if (!content.trim()) return [];

  return content
    .trim()
    .split("\n")
    .map((line) => {
      const [id, name, email, gender] = line.split(",");
      return { id, name, email, gender };
    });
}

function writeAll(employees) {
  const data = employees
    .map((e) => `${e.id},${e.name},${e.email},${e.gender}`)
    .join("\n");
  fs.writeFileSync(CSV_PATH, data + "\n", "utf8");
}

/* ---------- CRUD ---------- */
async function getAll() {
  return await readAll();
}

async function getById(id) {
  const all = await readAll();
  return all.find((e) => e.id === String(id)) || null;
}

async function add(data) {
  const all = await readAll();
  const emp = {
    id: data.id || String(Date.now()),
    name: data.name || "",
    email: data.email || "",
    gender: data.gender || "",
  };
  all.push(emp);
  writeAll(all);
  return emp;
}

async function update(id, data) {
  const all = await readAll();
  const index = all.findIndex((e) => e.id === String(id));
  if (index === -1) return null;

  all[index] = { ...all[index], ...data, id: String(id) };
  writeAll(all);
  return all[index];
}

async function remove(id) {
  const all = await readAll();
  const filtered = all.filter((e) => e.id !== String(id));
  if (filtered.length === all.length) return null;
  writeAll(filtered);
  return true;
}

async function removeMany(ids) {
  const all = await readAll();
  const idSet = new Set(ids.map(String));

  const remaining = [];
  const removed = [];

  for (const emp of all) {
    if (idSet.has(emp.id)) removed.push(emp);
    else remaining.push(emp);
  }

  writeAll(remaining);
  return removed;
}

module.exports = {
  getAll,
  getById,
  add,
  update,
  remove,
  removeMany,
};
