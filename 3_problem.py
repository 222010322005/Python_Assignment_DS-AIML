"""
Given an integer n, return the largest number that contains exactly n digits.
Example 1:
Input = 2
Output = 99
Example 2:
Input = 7
Output = 9999999
"""

import unittest


def largestNumber(nums):
    """
    ??? Write what needs to be done ???
    """
    a = 1
    for i in range(nums):
       a = a*10
    return(a-1)


# Add these test cases, and remove this placeholder

# 1. Test Cases from the Examples of Problem Statement
# 2. Other Simple Cases
# 3. Corner/Edge Cases
# 4. Large Inputs

# DO NOT TOUCH THE BELOW CODE
class TestlargestNumber(unittest.TestCase):

    def test_01(self):
        input_nums = 2
        output_nums = 99

        self.assertEqual(largestNumber(input_nums), output_nums)

    def test_02(self):
        input_nums = 7
        output_nums = 9999999

        self.assertEqual(largestNumber(input_nums), output_nums)

    def test_03(self):
        input_nums = 4
        output_nums = 9999

        self.assertEqual(largestNumber(input_nums), output_nums)


if __name__ == '__main__':
    unittest.main(verbosity=2)
