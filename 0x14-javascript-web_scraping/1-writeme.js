#!/usr/bin/node
// writes a string to file

const fileSy = require('fs');

fileSy.writeFile(process.argv[2], process.argv[3], 'utf-8',
  function (error) {
    if (error) {
      console.log(error);
    }
  });
