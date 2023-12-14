#!/usr/bin/node

const { argv } = require('process');

function factorial (n) {
  if (isNaN(parseInt(n)) || n === 0) {
    return 1;
  }
  return n * factorial(n - 1);
}

const num = parseInt(argv[2]);
console.log(factorial(num));
