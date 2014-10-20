import unittest


from solution import member_of_nth_fib_lists


class TestMemberOfFibList(unittest.TestCase):

    def test_correctness(self):
        self.assertFalse(member_of_nth_fib_lists([1, 2], [3, 4], [5, 6]))
        self.assertTrue(member_of_nth_fib_lists(
            [1, 2], [3, 4], [1, 2, 3, 4, 3, 4, 1, 2, 3, 4]))


if __name__ == "__main__":
    unittest.main()

