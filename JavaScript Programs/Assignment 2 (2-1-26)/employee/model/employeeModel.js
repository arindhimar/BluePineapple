class Employee {
  constructor({ id, name, email, gender }) {
    this.id = String(id);
    this.name = String(name);
    this.email = String(email);
    this.gender = String(gender);
  }

  static fromCSVLine(line) {
    const parts = line.trim().split(',');
    return new Employee({ id: parts[0], name: parts[1], email: parts[2], gender: parts[3] });
  }

  toCSVLine() {
    return `${this.id},${this.name},${this.email},${this.gender}`;
  }

  static validate(payload) {
    const errors = [];
    if (!payload.id) errors.push('id is required');
    if (!payload.name) errors.push('name is required');
    if (!payload.email) errors.push('email is required');
    else if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(payload.email)) errors.push('email is invalid');
    if (!payload.gender) errors.push('gender is required');
    return { valid: errors.length === 0, errors };
  }
}

module.exports = Employee;
