// JavaScript script that fetches the character name from
// from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json
$(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data, textStatus) {
    if (textStatus === 'success') {
        let movies = data.results;
        let index = 0;
        for (index in movies) {
            $('#list_movies').append('<br/>' + movies[index].title);
        }
    }
  });
});
