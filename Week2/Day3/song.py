class Song:
    MAX_RATE = 5
    MIN_RATE = 1

    def __init__(self, name, artist, album, length, bitrate):
        self.name = name
        self.artist = artist
        self.album = album
        self.raiting = 0
        self.length = length
        self.bitrate = bitrate

    def rate(self, value):
        if value < Song.MIN_RATE or value > Song.MAX_RATE:
            raise TypeError('Rate must be between {} and {}'
                            .format(Song.MIN_RATE, Song.MAX_RATE))
        else:
            self.raiting = value

    def _length(self):
        return "{:2d}:{:2d}".format(self.length // 60, self.length % 60)

