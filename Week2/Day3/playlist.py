class Playlist:
    SECONDS_IN_MINUTE = 60
    LOW_QUALITY = 128

    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song_name):
        for song in self.songs:
            if song.name is song_name:
                self.songs.remove(song)

    def total_length(self):
        length = 0
        for song in self.songs:
            length += song.length

        return '{:2d}:{:2d}'.format(length // Playlist.SECONDS_IN_MINUTE,
                                    length % Playlist.SECONDS_IN_MINUTE)

    def remove_disrated(self, raiting):
        for song in self.songs:
            if song.raiting <= raiting:
                self.songs.remove(song)

    def remove_bad_quality(self):
        for song in self.songs:
            if song.bitrate <= Playlist.LOW_QUALITY:
                self.songs.remove(song)

    def show_artists(self):
        artists = set()
        for song in self.songs:
            artists.add(song.artist)
        return artists

    def __str__(self):
        result = []
        for song in self.songs:
            song_info = '{} {} -{}'.format(song.artist, song.name, song._length())
            result.append(song_info)
        return '\n'.join(result)

