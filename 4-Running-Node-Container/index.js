const express = require('express')
const app = express()

app.get('/', function (req, res) {
  res.send('Hello there from express container!')
})

app.listen(3000)