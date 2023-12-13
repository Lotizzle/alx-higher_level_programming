#!/usr/bin/node

const { argv } = require('process');

const myVar1 = argv[2];
const myVar2 = argv[3];

console.log(myVar1 + ' is ' + myVar2);
