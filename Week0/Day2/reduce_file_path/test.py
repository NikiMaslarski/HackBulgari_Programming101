import unittest


from solution import reduce_file_path


class TestReduceFilePath(unittest.TestCase):

    def test_correctness(self):
        self.assertEqual(reduce_file_path('/etc/..//.././'), '/')
        self.assertEqual(reduce_file_path('/srv/www/'), '/srv/www')
        self.assertEqual(reduce_file_path('/niki/lqlq'), '/niki/lqlq')


if __name__ == '__main__':
    unittest.main()

