"""
You are given a two-digit integer n. Return the sum of its digits.
Example 1:
Input = 29
Output = 11
Example 2:
Input = 48
Output = 12
"""

import unittest


def addTwoDigits(nums):
    """
    ??? Write what needs to be done ???
    """
    sum = nums%10
    nums = nums//10
    sum = sum+nums%10
    return sum



# Add these test cases, and remove this placeholder

# 1. Test Cases from the Examples of Problem Statement
# 2. Other Simple Cases
# 3. Corner/Edge Cases
# 4. Large Inputs

# DO NOT TOUCH THE BELOW CODE
class TestaddTwoDigits(unittest.TestCase):

    def test_01(self):
        input_nums = 29
        output_nums = 11

        self.assertEqual(addTwoDigits(input_nums), output_nums)
    
    def test_02(self):
        input_nums = 48
        output_nums = 12

        self.assertEqual(addTwoDigits(input_nums), output_nums)

    def test_03(self):
        input_nums = 39
        output_nums = 12

        self.assertEqual(addTwoDigits(input_nums), output_nums)

    def test_04(self):
        input_nums = 45
        output_nums = 9

        self.assertEqual(addTwoDigits(input_nums), output_nums)


if __name__ == '__main__':
    unittest.main(verbosity=2)
