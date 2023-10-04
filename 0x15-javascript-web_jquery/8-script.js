$.get('https://swapi.co/api/films/?format=json', function (data) {
    let films = data.results;
      for (let film in films) {
        $('#list_movies').append('<li>' + films[film].title + '</li>');
      }
});