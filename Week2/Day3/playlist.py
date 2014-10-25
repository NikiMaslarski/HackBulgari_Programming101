import json

from song import Song


class Playlist:
    SECONDS_IN_MINUTE = 60
    LOW_QUALITY = 128

    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song_name):
        self.songs = [song for song in self.songs
                      if song.name != song_name]

    def total_length(self):
        length = 0
        for song in self.songs:
            length += song.length

        return '{:02d}:{:02d}'.format(length // Playlist.SECONDS_IN_MINUTE,
                                      length % Playlist.SECONDS_IN_MINUTE)

    def remove_disrated(self, raiting):
        self.songs = [song for song in self.songs
                      if song.raiting >= raiting]

    def remove_bad_quality(self):
        self.songs = [song for song in self.songs
                      if song.bitrate >= Playlist.LOW_QUALITY]

    def show_artists(self):
        artists = set()
        for song in self.songs:
            artists.add(song.artist)
        return artists

    def __str__(self):
        result = []
        for song in self.songs:
            song_info = '{} {} - {}'.format(song.artist,
                                            song.name,
                                            song._length())
            result.append(song_info)
        return '\n'.join(result)

    def save(self, file_name):
        file = open(file_name, 'w')
        json.dump(self.songs, file, default=lambda o: o.__dict__)
        file.close()

    @staticmethod
    def load(file_name):
        new_playlist = Playlist()
        loaded_text = json.load(open(file_name, 'r'))
        for song in loaded_text:
            new_song = Song(**song)
            new_playlist.add_song(new_song)
        return new_playlist

