import unittest

from fight import Fight
from hero import Hero
from orc import Orc
from weapon import Weapon


class TestFight(unittest.TestCase):

    def setUp(self):
        self.hero = Hero("Aiden", 500, "Daro Wonderer")
        self.orc = Orc("Thrall", 400, 1.4)
        weapon1 = Weapon("The Ash Bringer", 80, 0.5)
        weapon2 = Weapon('DoomHammer', 80, 0.5)
        self.hero.equip_weapon(weapon1)
        self.orc.equip_weapon(weapon2)

        self.fight = Fight(self.hero, self.orc)

    def test_simulate_fight(self):
        self.fight.simulate_fight()
        self.assertTrue(self.hero.is_alive() or self.orc.is_alive())
        self.assertFalse(self.orc.is_alive() and self.hero.is_alive())


if __name__ == "__main__":
    unittest.main()

