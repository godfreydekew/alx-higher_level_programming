$(document).ready(function(){ 
    $.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(data, status){
        $.each(data.results, function(index, film) {
            $("#list_movies").append("<li>" + film.title + "</li>");
        });
    });
});
