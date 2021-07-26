"""
Consider integer numbers from 0 to n - 1 written down along the circle in such a way that the distance between any two neighboring 
numbers is equal (note that 0 and n - 1 are neighboring, too).
Given n and firstNumber, find the number which is written in the radially opposite position to firstNumber.

Example1:
Input = [10,2]
Output = 7
Example1:
Input = [4,1]
Output = 3
"""

import unittest


def circleOfNumbers(n, firstNumber):
    """
    ??? Write what needs to be done ???
    """
    n = n//2
    if(firstNumber<n):
        return(n+firstNumber)
    elif(firstNumber>n):
        return(firstNumber-n)
    else:
        return 0


# Add these test cases, and remove this placeholder

# 1. Test Cases from the Examples of Problem Statement
# 2. Other Simple Cases
# 3. Corner/Edge Cases
# 4. Large Inputs

# DO NOT TOUCH THE BELOW CODE
class TestcircleOfNumbers(unittest.TestCase):

    def test_01(self):
        input_nums = [10,2]
        output_nums = 7

        self.assertEqual(circleOfNumbers(input_nums[0],input_nums[1]), output_nums)

    def test_02(self):
        input_nums = [18,6]
        output_nums = 15

        self.assertEqual(circleOfNumbers(input_nums[0],input_nums[1]), output_nums)

    def test_03(self):
        input_nums = [4,1]
        output_nums = 3

        self.assertEqual(circleOfNumbers(input_nums[0],input_nums[1]), output_nums)


if __name__ == '__main__':
    unittest.main(verbosity=2)
