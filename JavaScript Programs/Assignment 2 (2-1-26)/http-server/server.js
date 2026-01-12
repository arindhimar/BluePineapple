const http = require("http");
const fs = require("fs");
const path = require("path");
const formidable = require("formidable");

const port = 3000;
const uploads = path.join(__dirname, "uploads");

if (!fs.existsSync(uploads)) {
  fs.mkdirSync(uploads);
}

const server = http.createServer((req, res) => {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "GET,POST,OPTIONS");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type");

  if (req.method === "OPTIONS") {
    res.writeHead(204);
    return res.end();
  }

  if (req.method == "GET" && req.url=="/") {
    res.writeHead(200, { "Content-Type": "text/html" });
    return res.end(fs.readFileSync("index.html"));
  }

  if (req.method =="GET" && req.url == "/time") {
    res.writeHead(200, { "Content-Type": "application/json" });
    return res.end(
      JSON.stringify({
        australiaTimestamp: Date.now()
      })
    );
  }

  if (req.method == "POST" && req.url == "/upload") {
    const form = formidable.formidable({
      uploadDir: uploads,
      keepExtensions: true
    });

    form.parse(req, (err, fields, files) => {
      if (err) {
        res.writeHead(500);
        return res.end("Error");
      }

      if (!files.file) {
        res.writeHead(400);
        return res.end("No file");
      }

      const file = files.file;
      const name = file.originalFilename;
      const ext = path.extname(name);
      const base = path.basename(name, ext);
      const finalName = base.replace(/[^a-zA-Z0-9_-]/g, "_") + ext;

      fs.rename(file.filepath, path.join(uploads, finalName), () => {
        res.writeHead(200);
        res.end("Uploaded");
      });
    });

    return;
  }

  res.writeHead(404);
  res.end("Not found");
});

server.listen(port, () => {
  console.log("Server running on http://localhost:" + port);
});
