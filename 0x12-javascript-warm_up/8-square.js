#!/usr/bin/node

const { argv } = require('process');

const x = parseInt(argv[2]);
let result = '';

if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    result += 'X';
  }
}

for (let num = 0; num < x; num++) {
  console.log(result);
}
