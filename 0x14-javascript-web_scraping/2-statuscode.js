#!/usr/bin/node
// The Status Of Get request

const request = require('request');
const url = process.argv[2];

request.get(url, function (error, response) {
  if (error) {
    console.error(error); // Printing error to stderr
  } else {
    console.log('code:', response.statusCode); // Printing status code
  }
});
