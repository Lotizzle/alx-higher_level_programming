#!/usr/bin/node

const { argv } = require('process');

function add (a, b) {
  return a + b;
}

const int1 = parseInt(argv[2]);
const int2 = parseInt(argv[3]);

console.log(add(int1, int2));
