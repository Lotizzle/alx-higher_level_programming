#!/usr/bin/node

const { argv } = require('process');

function findSecondLargest (arr) {
  if (arr.length < 2) {
    return 0;
  }
  arr = arr.map(Number);
  arr = [...new Set(arr)];
  arr.sort((a, b) => b - a);
  return arr[1];
}

const args = argv.slice(2);
console.log(findSecondLargest(args));
