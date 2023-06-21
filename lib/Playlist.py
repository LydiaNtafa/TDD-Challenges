class Playlist():

    def __init__(self):
        self.tracklist = []

    def add_track(self, track):
        # Parameters:
        #   artist, songtitle : str
        # Returns:
        #   nothing
        # Side-effects
        #   adds the tracks to the tracklist directory
        if track == "":
            print("You cannot add a track with no Title")
        else: 
            self.tracklist.append(track)

    def display_list(self):
        return self.tracklist
    
