// Queries an API and fetches all movie titles then inserts them

let url = 'https://swapi.co/api/films/?format=json';
$.get(url, function (data) {
  let movies = data.results;
  for (let movie of movies) {
    $('ul#list_movies').append(`<li>${film.title}</li>`);
  }
});
