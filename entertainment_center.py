import media, fresh_tomatoes

bourne_identity = media.Movie("The Bourne Identity",
                        "Action spy thriller",
                        "https://upload.wikimedia.org/wikipedia/en/a/ae/BourneIdentityfilm.jpg",
                        "https://youtu.be/cD-uQreIwEk?t=27");

sexy_beast = media.Movie("Sexy Beast",
                         "Gangster movie",
                         "https://upload.wikimedia.org/wikipedia/en/9/90/Sexy_beast_ver1.jpg",
                         "https://youtu.be/99ihhUR8lkI");

crimson_tide = media.Movie("Crimson Tide",
                "A submarine drama",
                "https://upload.wikimedia.org/wikipedia/en/f/ff/Crimson_tide_movie_poster.jpg",
                "https://youtu.be/iS4I2Z1RBIw");

#crimson_tide.show_trailer()

movies = [bourne_identity, sexy_beast, crimson_tide]

fresh_tomatoes.open_movies_page(movies)
