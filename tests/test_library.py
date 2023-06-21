from lib.library import MusicLibrary
from lib.track import Track

"""
When we add two tracks
We get the tracks back in the track list
"""
def test_adding_2_tracks_getting_track_list():
    library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    library.add(track_1)
    library.add(track_2)
    assert library.tracks == [track_1, track_2]

"""
When we add two tracks
And we search for a word in the title
We get the matching track back
"""
def test_adding_2tracks_searching_for_word_from_title():
    library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    library.add(track_1)
    library.add(track_2)
    assert library.search_by_title_or_artist("Way") == [track_1]

"""
When we add two tracks
And we search for a small part of a word in the title
We get the matching track back
"""
def test_adding_2tracks_searching_for_part_of_word_from_title():
    library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    library.add(track_1)
    library.add(track_2)
    assert library.search_by_title_or_artist("lace") == [track_2]

"""
When we add two tracks
And we search for a word not in any track title
We get an empty list back
"""
def test_adding_2tracks_searching_for_asong_that_is_not_there():
    library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    library.add(track_1)
    library.add(track_2)
    assert library.search_by_title_or_artist("zzz") == []

"""
Given a track with a title and artist
#format returns a string like TITLE by ARTIST
"""
def test_track_format():
    track = Track("Higher Place", "Malevolence")
    assert track.format() == "Higher Place by Malevolence"

"""
When we add three tracks
And we search for an artist
We the list of the artist's songs
"""
def test_adding_2tracks_searching_for_artist():
    library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    track_3 = Track("Another One", "Terror")
    library.add(track_1)
    library.add(track_2)
    library.add(track_3)
    assert library.search_by_title_or_artist("Terror") == [track_1, track_3]