import unittest

import weapon


class TestWeapon(unittest.TestCase):

    def setUp(self):
        self.weapon = weapon.Weapon('Staff', 50, 0.5)

    def test_weapon_constructor(self):
        self.assertEqual(self.weapon.category, 'Staff')
        self.assertEqual(self.weapon.damage, 50)
        self.assertAlmostEqual(self.weapon.critical_strike_percent, 0.5)

    def test_wron_input(self):
        with self.assertRaises(ValueError):
            weapon.Weapon('Bow', 20, 3)

    def test_critical_hit(self):
        self.weapon.critical_strike_percent = 1
        self.assertTrue(self.weapon.critical_hit())

        self.weapon.critical_strike_percent = 0
        self.assertFalse(self.weapon.critical_hit())


if __name__ == '__main__':
    unittest.main()
