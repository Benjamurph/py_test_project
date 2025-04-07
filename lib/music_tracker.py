class MusicTracker():
    def __init__(self):
        self.track_history = []
    
    def add_track(self, track):
        self.track_history.append(track)

    def see_track_history(self):
        return self.track_history
    
    def see_unique_artists(self):
        unique_artists = {}
        for track in self.track_history:
            if track.artist not in unique_artists:
                unique_artists[track.artist] = [track]
            else:
                unique_artists[track.artist].append(track)
        return unique_artists
