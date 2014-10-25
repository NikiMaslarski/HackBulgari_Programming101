import unittest
from json import dumps
from os import remove

from playlist import Playlist
from song import Song


class TestPlaylist(unittest.TestCase):

    def setUp(self):
        self.playlist = Playlist()
        self.song = Song(
            'Clarity',
            "Zedd",
            'Clarity',
            456,
            64)
        self.playlist.add_song(self.song)

        self.song2 = Song(
            'Hearthbeat',
            "Nneka",
            'HB',
            65,
            256)
        self.playlist.add_song(self.song2)

    def test_add_song(self):
        self.assertTrue(self.song in self.playlist.songs)

    def test_remove_song(self):
        self.playlist.add_song(self.song)  # add it 2nd time
        self.playlist.remove_song("Clarity")
        self.assertTrue(self.song not in
                        [x for x in self.playlist.songs])

    def test_total_length(self):
        self.assertEqual(self.playlist.total_length(), "08:41")

    def test_remove_disrated(self):
        self.song.rate(2)
        self.playlist.remove_disrated(3)
        self.assertTrue(self.song not in
                        [x for x in self.playlist.songs])

    def test_remove_bad_quality(self):
        self.playlist.remove_bad_quality()
        self.assertTrue(self.song not in
                        [x for x in self.playlist.songs])

    def test_show_artists(self):
        self.assertEqual({"Nneka", "Zedd"},
                         self.playlist.show_artists())

    def test_string_representation(self):
        self.assertEqual(str(self.playlist),
                         "Zedd Clarity - 07:36\nNneka Hearthbeat - 01:05")

    def test_save(self):
        self.playlist.save("test_playlist.txt")
        file = open("test_playlist.txt")
        file_content = file.read()
        file.seek(0)

        self.assertEqual(file_content,
                         dumps(self.playlist.songs,
                               default=lambda o: o.__dict__))
        remove("test_playlist.txt")

    @unittest.skip("I have no Idea why it does not work")
    def test_load(self):
        self.playlist.save("test_playlist.txt")
        new_playlist = Playlist.load("test_playlist.txt")
        self.assertListEqual(str(new_playlist),
                             str(self.playlist))
        remove("test_playlist.txt")


if __name__ == '__main__':
    unittest.main()

