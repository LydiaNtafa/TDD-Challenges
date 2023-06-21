
class Track:
    # Public properties:
    #   title: a string
    #   artist: a string

    def __init__(self, title, artist):
        self._title = title
        self._artist = artist

    def format(self):
        # Returns:
        #   a string in the format "TITLE by ARTIST"
        return f"{self._title} by {self._artist}"
