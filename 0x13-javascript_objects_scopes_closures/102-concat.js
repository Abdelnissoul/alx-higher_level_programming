#!/usr/bin/node
const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const destFile = process.argv[4];

fs.readFile(fileA, 'utf8', (err, dataA) => {
  if (err) {
    console.error(err);
    return;
  }
  fs.readFile(fileB, 'utf8', (err, dataB) => {
    if (err) {
      console.error(err);
      return;
    }
    const concatenatedData = dataA + '\n' + dataB;
    fs.writeFile(destFile, concatenatedData, err => {
      if (err) {
        console.error(err);
        return;
      }
      console.log(`Files ${fileA} and ${fileB} have been concatenated to ${destFile}`);
    });
  });
});
