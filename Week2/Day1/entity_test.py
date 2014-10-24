import unittest

import entity
import weapon


class TestEntity(unittest.TestCase):

    def setUp(self):
        self.entity = entity.Entity("Aidan", 500)

    def test_entity_constructor(self):
        self.assertEqual(self.entity.name, 'Aidan')
        self.assertEqual(self.entity.health, 500)
        self.assertEqual(self.entity.weapon, False)

    def test_get_helth(self):
        self.assertEqual(self.entity.get_health(), self.entity.MAX_HEALTH)
        self.assertTrue(self.entity.is_alive())

        self.entity.health = -100
        self.assertFalse(self.entity.is_alive())

    def test_take_damage(self):
        self.entity.take_damage(200)
        self.assertEqual(self.entity.get_health(), self.entity.health)
        self.entity.take_damage(self.entity.MAX_HEALTH)
        self.assertEqual(self.entity.get_health(), 0)

    def test_take_healing(self):
        self.entity.take_damage(300)

        self.assertTrue(self.entity.take_healing(200))
        self.assertEqual(self.entity.get_health(), self.entity.MAX_HEALTH - 100)
        self.assertTrue(self.entity.take_healing(200))
        self.assertEqual(self.entity.get_health(), self.entity.MAX_HEALTH)
        self.entity.take_damage(self.entity.MAX_HEALTH)
        self.assertFalse(self.entity.take_healing(200))

    def test_has_weapon(self):
        self.assertFalse(self.entity.has_weapon())
        staff = weapon.Weapon("Staff", 50, 1)
        self.entity.equip_weapon(staff)
        self.assertTrue(self.entity.has_weapon())

    def test_equip_weapon(self):
        staff = weapon.Weapon("Staff", 50, 1)
        self.entity.equip_weapon(staff)
        self.assertEqual(self.entity.weapon, staff)

    def test_attack(self):
        self.assertEqual(self.entity.attack(), 0)
        staff = weapon.Weapon("Staff", 50, 1)
        self.entity.equip_weapon(staff)
        self.assertEqual(self.entity.attack(), self.entity.weapon.damage)


if __name__ == '__main__':
    unittest.main()

