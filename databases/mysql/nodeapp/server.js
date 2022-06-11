const express = require('express')
const app = express()
const mysql = require('mysql');
const bodyParser = require('body-parser')

app.set('view engine','ejs')
app.use(bodyParser.urlencoded({extended:true}))
app.use(express.static('public'))

const connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'thaumocracy',
  password : 'password',
  database : 'join_us',
  insecureAuth : true,
});
connection.connect()



app.get('/',function(req,res){
    const qry ='SELECT COUNT(*) as user_count FROM users'

    connection.query(qry, function (error, results) {
        if (error) {
            throw error
        };
        let count = results[0].user_count
        res.render('home',{data:count})
      });
})

app.post('/register',function(req,res){
    const person = {
        email:req.body.email
    }
    connection.query('INSERT INTO users SET ?',person,function(err,result){
        if(err){
            throw err
        }
        console.log(result)
        res.redirect('/')
    })
})
    

app.get('/shutka',(req,res) => (    
    res.send('shutka is not bloody working')
))

app.get('/num',(req,res) => (    
    res.send(`${Math.random()}`)
))







app.listen(3005,function(){
    console.log('Server running!')
})