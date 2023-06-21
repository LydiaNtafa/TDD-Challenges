
# from track import Track

class MusicLibrary:
    # Public properties:
    #   tracks: a list of strings representing tracks

    def __init__(self):
        self.tracks = []

    def add(self, track):
        self.tracks.append(track)
    
    def search_by_title_or_artist(self, keyword):
        # Parameters:
        #   keyword: a string
        # Returns:
        #   a list of Track instances with titles that include the keyword
        filtered_tracklist = []
        for track in self.tracks:
            if track.format().find(keyword) != -1:
                filtered_tracklist.append(track)
        
        return filtered_tracklist
    
