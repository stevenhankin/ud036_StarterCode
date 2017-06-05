import webbrowser


class Movie:
    """
    Attributes:
        title (str): Movie title
        storyline(str): Film synopsis
        poster_image_url(str): URL that links to an image of the film poster
                on the internet
        trailer_youtube_url(str): URL that links to a trailer for the film
                on youtube
    """
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ Launch the default browser and open the YouTube Trailer
        for this instance's film
        """
        webbrowser.open(self.trailer_youtube_url)
