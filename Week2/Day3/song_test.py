import unittest

from song import Song


class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song('Clarity', "Zedd", 'Clarity', 0, 456, 64)

        def test_constructor(self):
            self.assertEqual(self.song.name, 'Clarity')
            self.assertEqual(self.song.artist, 'Zedd')
            self.assertEqual(self.song.album, 'Clarity')
            self.assertEqual(self.song.raiting, 0)
            self.assertEqual(self.song.length, 0)
            self.assertEqual(self.song.bitrate, 64)


if __name__ == "__main__":
    unittest.main()
