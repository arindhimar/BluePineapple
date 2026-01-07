const http = require("http");
const helper = require("./helper.js")

const PORT = 3000;

const reqListener = function (req, res) {
    console.log("Welcome to NodeJS!!!")
};


const server = http.createServer(reqListener);

server.listen(PORT,()=>{
    console.log(`Running on localhost:${PORT}`)
    console.log(helper.getMessage())
})