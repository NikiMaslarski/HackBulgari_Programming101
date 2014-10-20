import unittest


from solution import is_an_bn


class TestAnBn(unittest.TestCase):

    def test_an_bn(self):
        self.assertTrue(is_an_bn("aaaabbbb"))
        self.assertFalse(is_an_bn("aabb "))
        self.assertFalse(is_an_bn("aabbb"))


if __name__ == "__main__":
    unittest.main()

