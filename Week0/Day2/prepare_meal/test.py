import unittest


from solution import prepare_meal


class TestPrepareMeal(unittest.TestCase):

    def test_prepare_meal(self):
        self.assertEqual(prepare_meal(3), 'spam')
        self.assertEqual(prepare_meal(45), "spam spam and eggs")
        self.assertEqual(prepare_meal(7), '')
        self.assertEqual(prepare_meal(15), "spam and eggs")


if __name__ == "__main__":
    unittest.main()

