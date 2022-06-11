const faker = require('faker')
const mysql = require('mysql');

const connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'thaumocracy',
  password : 'password',
  database : 'join_us',
  insecureAuth : true,
});

const data = []
const qry = 'INSERT INTO users (email,created_at) VALUES ?'

for(let i = 0;i < 500;i++){
  let person = []
  person.push(faker.internet.email())
  person.push(faker.date.past())
  data.push(person)
}
console.log(data)

connection.connect();
connection.query(qry,[data], function (error, results, fields) {
  if (error) throw error;
});




// connection.query(`INSERT INTO users SET ?`,person, function (error, results, fields) {
//   if (error) throw error;
//   console.log(results);
// });

connection.end();