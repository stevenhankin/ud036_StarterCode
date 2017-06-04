import media, fresh_tomatoes

bourne_identity = media.Movie("The Bourne Identity",
                              "A man is picked up by a fishing boat, bullet-riddled and suffering from amnesia, "
                              "before racing to elude assassins and regain his memory",
                              "https://upload.wikimedia.org/wikipedia/en/a/ae/BourneIdentityfilm.jpg",
                              "https://youtu.be/cD-uQreIwEk")

sexy_beast = media.Movie("Sexy Beast",
                         "Brutal gangster Don Logan recruits ""retired"" safecracker Gal for one last job",
                         "https://upload.wikimedia.org/wikipedia/en/9/90/Sexy_beast_ver1.jpg",
                         "https://youtu.be/99ihhUR8lkI")

crimson_tide = media.Movie("Crimson Tide",
                           "Mutiny on a US Nuclear Submarine",
                           "https://upload.wikimedia.org/wikipedia/en/f/ff/Crimson_tide_movie_poster.jpg",
                           "https://youtu.be/iS4I2Z1RBIw")

desperado = media.Movie("Desperado",
                        "A gunslinger is embroiled in a war with a local drug runner",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BYjA0NDMyYTgtMDgxOC00NGE0LWJkOTQtNDRjMjEzZmU0ZTQ3XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg", # nopep8
                        "https://youtu.be/ESSAlCrKUVg")

# Sort movies by title..
movies = sorted([bourne_identity, sexy_beast, crimson_tide, desperado], key=lambda movie: movie.title)

# ..and display in default browser
fresh_tomatoes.open_movies_page(movies)
