import webbrowser
import os
import re


def get_template_data(template_name):
    """Internal helper function

    The templates for the Header, content and tiles are
    stored in HTML "template" files within a resources
    subdirectory and are returned using this helper function

    :return: String of the template stored in file
    """
    return "".join(open('resources/' + template_name + '.html').readlines())


class Browser:
    """A Browser with a Fresh Tomatoes content

        Attributes:
            movies : array_like(str)
                     Array of movies

            main_page_head : scalar(str)

            main_page_content : scalar(str)

            movie_tile_content : scalar(str)
    """
    movies = []
    main_page_head = ""
    main_page_content = ""
    movie_tile_content = ""

    def __init__(self, movies):
        self.movies = movies
        # Styles and scripting for the page
        self.main_page_head = get_template_data('main_page_head')
        # The main page layout and title bar
        self.main_page_content = get_template_data('main_page_content')
        # A single movie entry html template
        self.movie_tile_content = get_template_data('movie_tile_content')

    def __create_movie_tiles_content(self):
        """The HTML content for each film in this section of the page"""
        content = ''
        for movie in self.movies:
            # Extract the youtube ID from the url
            youtube_id_match = re.search(
                r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
            youtube_id_match = youtube_id_match or re.search(
                r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
            trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                                  else None)

            # Append the tile for the movie with its content filled in
            content += self.movie_tile_content.format(
                movie_title=movie.title,
                storyline=movie.storyline,
                poster_image_url=movie.poster_image_url,
                trailer_youtube_id=trailer_youtube_id
            )
        return content

    def open_movies_page(self):
        """Generates a new HTML File for Fresh Tomatoes contents and opens in the default webbrowser"""
        # Create or overwrite the output file
        output_file = open('fresh_tomatoes.html', 'w')

        # Replace the movie tiles placeholder generated content
        rendered_content = self.main_page_content.format(
            movie_tiles=self.__create_movie_tiles_content())

        # Output the file
        output_file.write(self.main_page_head + rendered_content)
        output_file.close()

        # open the output file in the browser (in a new tab, if possible)
        url = os.path.abspath(output_file.name)
        webbrowser.open('file://' + url, new=2)
