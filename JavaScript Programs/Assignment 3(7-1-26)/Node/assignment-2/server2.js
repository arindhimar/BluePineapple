const http = require("http");
const fs = require("fs");
const fsPromises = fs.promises;

const PORT = 3000;

const sampleText =
  "This is text which is added every time this script runs!!\n";

// ---------- SYNC VERSION ----------
const appendToFile = function () {
  try {
    fs.appendFileSync("./assignment-2/log.txt", sampleText, "utf8");
    console.log("New data has been added to the file!!");
    readFromFile();
  } catch (err) {
    console.error(err);
  }
};

const readFromFile = function () {
  try {
    const fileData = fs.readFileSync("./assignment-2/log.txt", "utf8");
    console.log("File contents:\n", fileData);
  } catch (err) {
    console.error(err);
  }
};

// ---------- ASYNC VERSION ----------
const appendToFileAsync = async function () {
  try {
    await fsPromises.appendFile("./assignment-2/log.txt", sampleText, "utf8");
    console.log("New data has been added to the file!!");
    await readFromFileAsync();
  } catch (err) {
    console.error(err);
  }
};

const readFromFileAsync = async function () {
  try {
    const fileData = await fsPromises.readFile(
      "./assignment-2/log.txt",
      "utf8"
    );
    console.log("File contents:\n", fileData);
  } catch (err) {
    console.error(err);
  }
};

// ---------- nextTick,setTimeOut,SetImmidiate ----------

const executionOfFunction = function () {
  console.log("starting this one is synhronous");

  setTimeout(() => {
    console.log("This is right here is using setTimeout with 1 seconds!!");
  }, 1000);

  setImmediate(() => {
    console.log("This is right here is using setImmediate!!");
  });

  process.nextTick(() => {
    console.log("This is right here is using process.nextTick!!");
  });

  console.log("ending this one is synhronous");
};

// ---------- SERVER ----------
const reqListener = function (req, res) {
  res.end("Server is running!\n");
};

const server = http.createServer(reqListener);

server.listen(PORT, () => {
  console.log(`Server is running at http://localhost:${PORT}`);

  //   appendToFile();
//   appendToFileAsync();
    executionOfFunction();
});
