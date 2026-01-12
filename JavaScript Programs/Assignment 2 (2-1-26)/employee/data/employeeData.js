const { json } = require('body-parser');
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

  const data =  new Promise((resolve, reject) => {
    fs.readFile(CSV_PATH, 'utf8', (err, content) => {
      if (err) {
        return reject(err);
      }
      const employees = content.trim().split('\n').filter(line => line).map(line => {
        const parts = line.split(',');
        return {
          id: parts[0],
          name: parts[1],
          email: parts[2],
          gender: parts[3]
        };
      });
      resolve(employees);
    });
  });

  return data;
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
  // console.log("data received in add function:", JSON.stringify(data));
  //data is in json format
  // let tempNewData = JSON.parse(data);
  console.log("data in add function:", data);
  
  const emp = {
    id: data.id || String(Date.now())  ,
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
