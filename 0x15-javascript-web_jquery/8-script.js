/*
Write a JavaScript script that fetches and lists the title for all movies
by using this URL.
All movie titles must be list in the HTML tag UL#list_movies
*/

$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  $.each(data.results, function (index, value) {
    $('UL#list_movies').append('<li>' + value.title + '</li>');
  });
});
