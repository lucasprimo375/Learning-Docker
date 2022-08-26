const prompt = require('prompt-sync')();
const fs = require('fs');

const file_name = prompt('Enter file name: ');

const file_content = prompt('Enter file content: ');

fs.writeFile(file_name + '.txt', file_content, function (err) {
    if (err) throw err;
    
    console.log('Content saved inside the file!');
});