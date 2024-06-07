#!/usr/bin/node
const request = require('request');

function printNames (movieId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
  request(url, (error, response, body) => {
    if (error) {
      console.error(error);
    }

    if (response.statusCode !== 200) {
      console.error(`Request failed with code ${response.statusCode}`);
    }

    const data = JSON.parse(body);
    const characters = data.characters;

    for (const personURL of characters) {
      request(personURL, (error, response, body) => {
        if (error) {
          console.error(error);
        }

        if (response.statusCode !== 200) {
          console.error(`Request failed with code ${response.statusCode}`);
        }
        const person = JSON.parse(body);
        console.log(person.name);
      });
    }
  });
}

const movieId = process.argv[2];
printNames(movieId);
