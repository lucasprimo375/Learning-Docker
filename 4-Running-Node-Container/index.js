const express = require('express')
const process = require('process')

process.on('SIGINT', () => {
    console.log('Hello there! Application is being interrupted!')
    process.exit(0)
})

process.on('SIGTERM', () => {
    console.log('Hello there! Application is being terminated!')
    process.exit(0)
})

const app = express()

app.get('/', function (req, res) {
  res.send('Hello there from express container!')
})

app.listen(3000)