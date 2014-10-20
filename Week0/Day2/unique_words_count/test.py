import unittest


from solution import unique_words_count


class TestUniqueWordsCounter(unittest.TestCase):

    def test_correctness(self):
        self.assertEqual(unique_words_count(['this', 'is', 'madness', 'no', 'this' 'is', 'Sparta']), 6)


if __name__ == '__main__':
    unittest.main()

