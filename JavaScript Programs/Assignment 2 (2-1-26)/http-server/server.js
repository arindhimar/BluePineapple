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

  if (req.method == "GET" && req.url == "/") {
    res.writeHead(200, { "Content-Type": "text/html" });
    return res.end(fs.readFileSync("index.html"));
  }

  // if (req.method === "GET" && req.url === "/time") {
  //   const now = new Date();
  //   const australiaTime = now.toLocaleString("en-AU", {
  //     timeZone: "Australia/Sydney",
  //   });
  //   res.writeHead(200, { "Content-Type": "application/json" });
  //   return res.end(
  //     JSON.stringify({
  //       australiaTime,
  //     })
  //   );
  // }

  if (req.method === "GET" && req.url.startsWith("/time-stream")) {
    res.writeHead(200, {
      "Content-Type": "text/event-stream",
      "Cache-Control": "no-cache",
      Connection: "keep-alive",
    });
    const sendTime = () => {
      const australiaTime = new Date().toLocaleString("en-AU", {
        timeZone: "Asia/Kolkata",
      });
      res.write(`data: ${australiaTime}\n\n`);
    };

    sendTime();
    const interval = setInterval(sendTime, 1000);
    req.on("close", () => clearInterval(interval));

    return;
  }

  if (req.method === "POST" && req.url === "/upload") {
    const form = formidable.formidable({
      uploadDir: uploads,
      keepExtensions: true,
      filename: (name, ext, part) => {
        const safeName = part.originalFilename
          .replace(/\s+/g, "_")
          .replace(/[^a-zA-Z0-9_.-]/g, "");
        return safeName;
      },
    });

    form.parse(req, (err, fields, files) => {
      if (err) {
        res.statusCode = 500;
        return res.end("Error");
      }

      if (!files.file) {
        res.statusCode = 400;
        return res.end("No file");
      }

      const file = files.file;
      const name = file.originalFilename;
      const ext = path.extname(name);
      const base = path.basename(name, ext);
      const finalName = base.replace(/[^a-zA-Z0-9_-]/g, "_") + ext;

      fs.rename(file.filepath, path.join(uploads, finalName), () => {
        res.statusCode = 200;
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
