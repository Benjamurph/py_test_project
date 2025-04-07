from lib.music_tracker import *
from lib.track import *

def test_music_tracker():
    music_tracker1 = MusicTracker()
    track1 = Track('Waterloo', 'ABBA')
    track2 = Track('Take A Chance On Me', 'ABBA')
    track3 = Track('Dirty Work', 'Steely Dan')
    music_tracker1.add_track(track1)
    assert music_tracker1.see_track_history() == [track1]
    music_tracker1.add_track(track2)
    assert music_tracker1.see_track_history() == [track1, track2]
    music_tracker1.add_track(track3)
    assert music_tracker1.see_unique_artists() == {'ABBA': [track1, track2], 'Steely Dan': [track3]}
