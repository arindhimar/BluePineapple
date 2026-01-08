


class Calculator {
  constructor(initialNum = 0) {
    this.value = initialNum;
  }

  add(num) {
    this.value += num;
    return this;
  }

  subtract(num) {
    this.value -= num;
    return this;
  }

  multiply(num) {
    this.value *= num;
    return this;
  }

  divide(num) {
    this.value /= num;
    return this;
  }

  getResult() {
    return this.value;
  }
}

module.exports = {Calculator}
