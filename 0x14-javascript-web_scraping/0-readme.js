#!/usr/bin/node
// importing and reading the file

const file_s = require('fs');
file_s.readFile(process.argv[2], 'utf-8',
  function (error, data) {
    if (error) {
      console.log(error);
      return;
    }
    console.log(data);
  });
