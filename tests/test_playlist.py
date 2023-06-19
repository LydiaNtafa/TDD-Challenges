from lib.Playlist import Playlist

'''
When there have been no added tracks
Returns an empty list
'''
def test_initially_has_no_tracks():
    playlist = Playlist()
    assert playlist.display_list() == []

'''
When there is 1 track added
The track is reflected on the list
'''
def test_1track_added():
    playlist = Playlist()
    playlist.add_track("PoS - Entropia")
    assert playlist.display_list() == ["PoS - Entropia"]

'''
When there are multiple tracks added
The tracsk are reflected on the list
'''
def test_3tracks_added():
    playlist = Playlist()
    playlist.add_track("PoS - Entropia")
    playlist.add_track("BLS - Stillborn")
    playlist.add_track("Me - My first Demo")
    assert playlist.display_list() == ["PoS - Entropia", "BLS - Stillborn", "Me - My first Demo"]

'''
When there is an empty track added
it is NOT reflected in the list
'''
def test_empty_track_added():
    playlist = Playlist()
    playlist.add_track("PoS - Entropia")
    playlist.add_track("")
    assert playlist.display_list() == ["PoS - Entropia"]
