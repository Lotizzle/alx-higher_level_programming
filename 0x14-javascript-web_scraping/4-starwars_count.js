#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = '18';

request(apiUrl, function (error, response, body) {
  if (error) {
    console.log('Error:', error);
  } else if (response.statusCode !== 200) {
    console.log('Request failed with status code:', response.statusCode);
  } else {
    const films = JSON.parse(body).results;
    let count = 0;

    films.forEach(film => {
      const characters = film.characters;
      if (characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
        count++;
      }
    });
    console.log(count);
  }
});
