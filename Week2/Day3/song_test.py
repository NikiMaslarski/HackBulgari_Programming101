import unittest

from song import Song


class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song(
            'Clarity',
            "Zedd",
            'Clarity',
            456,
            64)

    def test_constructor(self):
        self.assertEqual(self.song.name, 'Clarity')
        self.assertEqual(self.song.artist, 'Zedd')
        self.assertEqual(self.song.album, 'Clarity')
        self.assertEqual(self.song.raiting, 0)
        self.assertEqual(self.song.length, 456)
        self.assertEqual(self.song.bitrate, 64)

    def test_rate(self):
        self.assertEqual(self.song.raiting, 0)
        self.song.rate(4)
        self.assertEqual(self.song.raiting, 4)
        with self.assertRaises(TypeError):
            self.song.rate(10)


if __name__ == "__main__":
    unittest.main()

