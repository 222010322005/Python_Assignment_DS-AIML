"""
Given a divisor and a bound, find the largest integer N such that:

N is divisible by divisor.
N is less than or equal to bound.
N is greater than 0.
It is guaranteed that such a number exists.

Example1:
Input = [3,10]
Output = 9
Example2:
Input = [10,50]
Output = 50
"""

import unittest


def maxMultiple(divisor, bound):
    """
    ??? Write what needs to be done ???
    """
    return(bound-(bound%divisor))


# Add these test cases, and remove this placeholder

# 1. Test Cases from the Examples of Problem Statement
# 2. Other Simple Cases
# 3. Corner/Edge Cases
# 4. Large Inputs

# DO NOT TOUCH THE BELOW CODE
class TestmaxMultiple(unittest.TestCase):

    def test_01(self):
        input_nums = [3,10]
        output_nums = 9

        self.assertEqual(maxMultiple(input_nums[0],input_nums[1]), output_nums)
    
    def test_02(self):
        input_nums = [10,50]
        output_nums = 50

        self.assertEqual(maxMultiple(input_nums[0],input_nums[1]), output_nums)
    
    def test_03(self):
        input_nums = [7,100]
        output_nums = 98

        self.assertEqual(maxMultiple(input_nums[0],input_nums[1]), output_nums)


if __name__ == '__main__':
    unittest.main(verbosity=2)
