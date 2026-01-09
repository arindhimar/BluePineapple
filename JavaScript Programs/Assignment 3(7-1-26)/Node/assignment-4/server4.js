const http = require("http");
const PORT = 3000;

const fetchData = async () => {
  try {
    const response = await fetch("https://jsonplaceholder.typicode.com/posts");
    const data = await response.json();
    console.log(data)
    for (let i = 0; i < 5; i++) {
        console.log("Title : "+data[i].title);
        console.log("Body : "+data[i].body);
    }
  } catch (err) {
    console.error(err);
  }
};

const fetchMultipleApi = async function (){
    const urls =[
        "https://jsonplaceholder.typicode.com/posts",
        "https://jsonplaceholder.typicode.com/posts"
    ]

    try{
        const promises = urls.map(url=>fetch(url));

        const responses = await Promise.all(promises);

        const tempJsonData = responses.map(tempData=>{
            return tempData.json();
        })

        const jsonData = await Promise.all(tempJsonData);

        console.log(jsonData);

    }
    catch(err){
        console.error(err);
    }

}

const server = http.createServer((req, res) => {});

server.listen(PORT, () => {
//   fetchData();
fetchMultipleApi();
  console.log(`Server is running at http://localhost:${PORT}`);
});
