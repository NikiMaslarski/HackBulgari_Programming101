import unittest


from solution import goldbach


class TestGoldblach(unittest.TestCase):

    def test_goldblach(self):
        self.assertEqual(goldbach(4), [(2, 2)])
        self.assertEqual(goldbach(100), [(3, 97), (11, 89), (17, 83),
                                         (29, 71), (41, 59), (47, 53)])


if __name__ == '__main__':
    unittest.main()

