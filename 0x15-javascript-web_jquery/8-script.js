// a JavaScript script that fetches and lists
//the title for all movies by using this URL:
// https://swapi-api.alx-tools.com/api/films/?format=json

$.get('https://swapi.co/api/films/?format=json', function (films, status) {
  const data = films.results;
  for (const item of data) {
    $('ul#list_movies').append('<li>' + item.title + '</li>');
  }
});