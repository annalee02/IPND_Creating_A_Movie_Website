import webbrowser

class Movie():
    """This class is to enable other .py files to create instances and to use a pre-defined function"""
    def __init__(self, movie_title, release_year, movie_storyline, poster_image, trailer_youtube):
        """How to call the input"""
        self.title = movie_title
        self.release = release_year
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

#print Movie.__doc__
#print Movie.__init__.__doc__ 
