import unittest
import main


class TestMain(unittest.TestCase):
    def test_genStart(self):
        '''Start point is generated'''
        param = 5
        result = main.genStart(param)
        self.assertEqual(result, 5)

    def test_genStop(self):
        '''End point is generated'''
        param = 10
        result = main.genStop(param)
        self.assertEqual(result, 10)

    def test_getPoint(self):
        '''Random point is correctly generated'''
        p1 = 1
        p2 = 10
        result = main.getPoint(p1, p2)
        self.assertTrue(p1 < result < p2)

    def test_checkAnswer(self):
        '''Correct guess'''
        p1 = 1
        p2 = 5
        p3 = 10
        result = main.checkAnswer(p1, p2, p3)
        self.assertTrue(result)

    def test_checkAnswer(self):
        '''Correct error guess'''
        p1 = 5
        p2 = 3
        p3 = 1
        result = main.checkAnswer(p1, p2, p3)
        self.assertFalse(result)


unittest.main()
