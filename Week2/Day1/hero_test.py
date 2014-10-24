import unittest

import hero


class TestHero(unittest.TestCase):

    def setUp(self):
        self.hero = hero.Hero("Aidan", 500, "Dark Wanderer")

    def test_hero_constructor(self):
        self.assertEqual(self.hero.name, "Aidan")
        self.assertEqual(self.hero.health, 500)
        self.assertEqual(self.hero.nickname, "Dark Wanderer")

    def test_known_as(self):
        self.assertEqual(self.hero.known_as(), "Aidan the Dark Wanderer")


if __name__ == '__main__':
    unittest.main()

