import unittest
import main


class TestMain(unittest.TestCase):
    def setUp(self):
        print('Starting do_stuff testing:')

    def test_do_stuff(self):
        '''Checks for correct number'''
        param = 10
        result = main.do_stuff(param)
        self.assertEqual(result, 15)

    def test_do_wrong(self):
        '''Checks for string input'''
        param = 'string'
        result = main.do_stuff(param)
        self.assertIsInstance(result, ValueError)

    def test_do_none(self):
        '''Checks for None input'''
        param = None
        result = main.do_stuff(param)
        self.assertEqual(result, 'Enter a number')

    def tearDown(self):
        print('Finishing with test')


if __name__ == '__main__':
    unittest.main()
