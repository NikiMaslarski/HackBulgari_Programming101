import unittest

from solution import count_words


class TestCountWords(unittest.TestCase):

    def test_counting_words(self):
        self.assertEqual(count_words(["apple", "banana", "apple", "pie"]),
                         {'apple': 2, 'pie': 1, 'banana': 1})

        self.assertEqual(count_words(["a", 'a', 'a', 'b']), {'a': 3, 'b': 1})
        self.assertNotEqual(count_words(['v']), {"v": 0})


if __name__ == '__main__':
    unittest.main()

