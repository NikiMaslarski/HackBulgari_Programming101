import unittest

import orc
import weapon


class TestOrc(unittest.TestCase):

    def setUp(self):
        self.orc = orc.Orc('Thrall', 500, 1.75)

    def test_orc_constructor(self):
        self.assertEqual(self.orc.health, 500)
        self.assertEqual(self.orc.name, 'Thrall')
        self.assertAlmostEqual(self.orc.berserk_factor, 1.75)

    def test_orc_berserk(self):
        orc_ = orc.Orc("Thrall", 500, 5)
        self.assertAlmostEqual(orc_.berserk_factor, 2)

        orc_ = orc.Orc("Thrall", 500, 0.89)
        self.assertAlmostEqual(orc_.berserk_factor, 1)

    def test_orc_attack(self):
        sword = weapon.Weapon("The Ash Bringer", 5000, 1)
        self.orc.equip_weapon(sword)
        self.assertAlmostEqual(self.orc.attack(), 5000 * self.orc.berserk_factor)


if __name__ == '__main__':
    unittest.main()

