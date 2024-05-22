#!/usr/bin/node
// Prints all characters of a Star Wars movie

const request = require('request');

const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./101-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(movieUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch movie details:', response.statusCode);
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  const fetchCharacterNames = async () => {
    for (const characterUrl of characters) {
      await new Promise((resolve) => {
        request(characterUrl, (error, response, body) => {
          if (error) {
            console.error('Error:', error);
            resolve();
            return;
          }

          if (response.statusCode !== 200) {
            console.error('Failed to fetch character details:', response.statusCode);
            resolve();
            return;
          }

          const character = JSON.parse(body);
          console.log(character.name);
          resolve();
        });
      });
    }
  };

  fetchCharacterNames();
});
