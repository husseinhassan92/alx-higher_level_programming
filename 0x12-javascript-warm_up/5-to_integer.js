#!/usr/bin/node

const num = parseInt(process.argv[2], 10);
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
