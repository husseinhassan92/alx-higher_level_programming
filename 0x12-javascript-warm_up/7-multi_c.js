#!/usr/bin/node

const num = parseInt(process.argv[2]);
if (isNaN (num)) {
    console.log('Missing number of occurrences');
}
let x = 0;
while (x < process.argv[2]) {
    console.log('C is fun');
    x++;
}
