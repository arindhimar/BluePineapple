const http = require("http");
const { Calculator } = require("./Calculator");

const PORT = 3000;
const calc = new Calculator();

const fetchData = () => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      fetch("https://jsonplaceholder.typicode.com/posts")
        .then(res => res.json())
        .then(data => resolve(data))
        .catch(err => reject(err));
    }, 2000);
  });
};

const server = http.createServer((req, res) => {
  fetchData()
    .then(data => {
      console.log("Fetched posts:", data.length);

      const result = calc
        .add(10)
        .subtract(5.5)
        .multiply(1)
        .divide(1)
        .getResult();

      console.log("Calculator result:", result);
    })
    .catch(error => {
      console.error("Fetch error:", error);
    });
});

server.listen(PORT, () => {
  console.log(`server is running at http://localhost:${PORT}`);
});
