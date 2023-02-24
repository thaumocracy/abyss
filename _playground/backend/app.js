const Express = require("express");
const app = Express();

counter = 0;
dict = {};

app.get("/", (req, res) => {
  dict[counter] = "Hello World";
  counter++;
  res.send("Hello World");
});

app.get("/dict", (req, res) => {
  res.json(dict);
});
app.listen(3001, () => {
  console.log("Server running at port 3001");
});
