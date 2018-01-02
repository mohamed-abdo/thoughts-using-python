import sys
import unittest

class Solution():
    def get_greatest_number(self, number):
        if not isinstance(number, int):
            raise TypeError('{0} is mismatched type'.format(number))
        if number > sys.maxsize:
            raise ValueError('{0} is out of the limits'.format(number))
        if number < - sys.maxsize:
            raise ValueError('{0} is out of the limits'.format(number))
        #get the absolute value
        if number < 0 :
            number = number *-1
        #of one digit, return this digit
        if len(str(number)) == 1:
            return number
        """
        procedures
        1- parse number as string
        2- iterate over the string into array
        3- descending sort the array
        4- join the array into string
        5- parse string into integer

        """
        return int(''.join(sorted(str(number), reverse=True)))

class test_Solution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_oneNumber(self):
        self.assertEqual(self.solution.get_greatest_number(3), 3, 'one digit test failed')
    
    def test_ManyNumbers(self):
            self.assertEqual(self.solution.get_greatest_number(123456789), 987654321, 'many digits test failed')
    
    def test_minValue(self):
        self.assertEqual(self.solution.get_greatest_number(-sys.maxsize), 8776444321)

    def test_maxValue(self):
            self.assertEqual(self.solution.get_greatest_number(sys.maxsize), 8776444321)

    def test_raiseTypeError(self):
        self.assertRaises(TypeError,self.solution.get_greatest_number, 'd245', 'type check failed')

    def test_raiseTypeErrorWithNone(self):
        self.assertRaises(TypeError,self.solution.get_greatest_number, None, 'type check failed')

    def test_raiseValueWithMaxValueError(self):
        self.assertRaises(ValueError,self.solution.get_greatest_number, sys.maxsize + 1)
        
    def test_raiseValueWithMinValueError(self):
        self.assertRaises(ValueError,self.solution.get_greatest_number,(- sys.maxsize) - 1)
    def tearDown(self):
        self.solution=None

if __name__ == '__main__':
    unittest.main()
