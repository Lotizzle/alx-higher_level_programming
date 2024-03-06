#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[3];
const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Request failed with status code:', response.statusCode);
  } else {
    const text = body;

    fs.writeFile(filePath, text, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
