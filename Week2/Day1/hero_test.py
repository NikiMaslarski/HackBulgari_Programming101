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

    def test_get_helth(self):
        self.assertEqual(self.hero.get_health(), self.hero.MAX_HEALTH)
        self.assertTrue(self.hero.is_alive())

        self.hero.health = -100
        self.assertFalse(self.hero.is_alive())

    def test_take_damage(self):
        self.hero.take_damage(200)
        self.assertEqual(self.hero.get_health(), self.hero.health)

    def test_take_healing(self):
        self.hero.take_damage(300)

        self.assertTrue(self.hero.take_healing(200))
        self.assertEqual(self.hero.get_health(), self.hero.MAX_HEALTH - 100)
        self.assertTrue(self.hero.take_healing(200))
        self.assertEqual(self.hero.get_health(), self.hero.MAX_HEALTH)
        self.hero.take_damage(self.hero.MAX_HEALTH)
        self.assertFalse(self.hero.take_healing(200))


if __name__ == '__main__':
    unittest.main()

