import unittest

import orc


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

    def test_get_helth(self):
        self.assertEqual(self.orc.get_health(), self.orc.MAX_HEALTH)
        self.assertTrue(self.orc.is_alive())

        self.orc.health = -100
        self.assertFalse(self.orc.is_alive())

    def test_take_damage(self):
        self.orc.take_damage(200)
        self.assertEqual(self.orc.get_health(), self.orc.health)

    def test_take_healing(self):
        self.orc.take_damage(300)

        self.assertTrue(self.orc.take_healing(200))
        self.assertEqual(self.orc.get_health(), self.orc.MAX_HEALTH - 100)
        self.assertTrue(self.orc.take_healing(200))
        self.assertEqual(self.orc.get_health(), self.orc.MAX_HEALTH)
        self.orc.take_damage(self.orc.MAX_HEALTH)
        self.assertFalse(self.orc.take_healing(200))

if __name__ == '__main__':
    unittest.main()

