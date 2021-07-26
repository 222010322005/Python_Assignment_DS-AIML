"""
Given integers a and b, determine whether the following pseudocode results in an infinite loop
while a is not equal to b do
  increase a by 1
  decrease b by 1
Assume that the program is executed on a virtual machine which can store arbitrary long numbers and execute forever.
Example 1:
Input = [2,6]
Output = False
Example 2:
Input = [2,3]
Output = True
"""

import unittest


def isInfiniteProcess(a, b):
    """
    ??? Write what needs to be done ???
    """
    c = (b - a)//2
    if a>b:
        return True
    elif a==b:
        return False
    elif (a+c==b-c):
        return False
    else:
        return True


# Add these test cases, and remove this placeholder

# 1. Test Cases from the Examples of Problem Statement
# 2. Other Simple Cases
# 3. Corner/Edge Cases
# 4. Large Inputs

# DO NOT TOUCH THE BELOW CODE
class TestisInfiniteProcess(unittest.TestCase):

    def test_01(self):
        input_nums = [2, 3]
        output = True

        self.assertEqual(isInfiniteProcess(input_nums[0],input_nums[1]), output)

    def test_01(self):
        input_nums = [2, 6]
        output = False

        self.assertEqual(isInfiniteProcess(input_nums[0],input_nums[1]), output)

    def test_01(self):
        input_nums = [0, 1]
        output = True

        self.assertEqual(isInfiniteProcess(input_nums[0],input_nums[1]), output)

    def test_01(self):
        input_nums = [2, 10]
        output = False

        self.assertEqual(isInfiniteProcess(input_nums[0],input_nums[1]), output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
