#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Invalid status code:', response.statusCode);
  } else {
    const filmData = JSON.parse(body);
    const charactersUrls = filmData.characters;
    const charactersPromises = charactersUrls.map(url => new Promise((resolve, reject) => {
      request(url, function (error, response, body) {
        if (error) {
          reject(error);
        } else if (response.statusCode !== 200) {
          reject(`Invalid status code: ${response.statusCode}`);
        } else {
          const characterData = JSON.parse(body);
          resolve(characterData.name);
        }
      });
    }));

    Promise.all(charactersPromises)
      .then(characters => {
        characters.forEach(character => console.log(character));
      })
      .catch(error => {
        console.error('Error fetching character data:', error);
      });
  }
});

