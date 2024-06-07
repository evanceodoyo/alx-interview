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

    const charactersURLs = JSON.parse(body).characters;

    const names = charactersURLs.map(
      url => new Promise((resolve, reject) => {
        request(url, (promiseError, resp, charReqBody) => {
          if (promiseError) {
            reject(promiseError);
          }
          resolve(JSON.parse(charReqBody).name);
        });
      })
    );
    Promise.all(names)
      .then(names => console.log(names.join('\n')))
      .catch(err => console.error(err));
  });
}

const movieId = process.argv[2];
printNames(movieId);
