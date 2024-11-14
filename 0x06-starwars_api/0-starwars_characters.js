#!/usr/bin/node

const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, res, body) {
  if (err) throw err;
  const actor = JSON.parse(body).characters;
  Order(actor, 0);
});
const Order = (actor, z) => {
  if (z === actor.length) return;
  request(actor[z], function (err, res, body) {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    Order(actor, z + 1);
  });
};
