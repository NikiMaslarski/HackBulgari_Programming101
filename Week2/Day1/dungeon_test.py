import unittest

from dungeon import Dungeon


class TestDungeon(unittest.TestCase):

    def SetUp(self):
        test_file = open("test_dungeon.txt", 'w')
        test_file.write(
"""S.##......
#.##..###.
#.###.###.
#.....###.
###.#####S""")

        self.dungeon = Dungeon(test_file)



if __name__ == '__main__':
    unittest.main()
