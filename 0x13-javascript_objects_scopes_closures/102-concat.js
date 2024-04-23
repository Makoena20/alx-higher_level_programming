#!/usr/bin/node

const fs = require('fs');
const { argv } = require('process');

const [, , file1, file2, dest] = argv;

const content1 = fs.readFileSync(file1, 'utf-8');
const content2 = fs.readFileSync(file2, 'utf-8');

fs.writeFileSync(dest, content1 + content2);

