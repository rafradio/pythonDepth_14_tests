from queensTest import calc

import unittest
class TestCaseName(unittest.TestCase):

    def setUp(self):
        # self.expected_values = input('введите значения: ').split(' ')
        self.expected_values = ['a8', 'b2', 'c5', 'd3', 'e1', 'f7', 'g4', 'h6']

    def test_method(self):
        # expected_values = ['a8', 'b2', 'c5', 'd3', 'e1', 'f7', 'g4', 'h6']
        
        self.assertIn(self.expected_values, calc(0, [], [], [], []), 'Данного ответа нет')
    

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestCaseName('test_method'))
    return suite

if __name__ == '__main__':
    # unittest.main()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())