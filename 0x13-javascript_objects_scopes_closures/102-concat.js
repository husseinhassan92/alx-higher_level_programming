#!/usr/bin/node
const fs = require('fs');
const filea = fs.readFileSync(process.argv[2], 'utf8');
const fileb = fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], filea + fileb);
