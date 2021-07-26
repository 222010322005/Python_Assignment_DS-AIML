"""
You're given three integers, a, b and c. It is guaranteed that two of these integers are equal to each other. 
What is the value of the third integer?
Example 1:
Input:
a=2
b=7
c=2
Output:
7
Example 2:
Input:
a=3
b=2
c=2
Output:
3

"""

import unittest


def extraNumber(a , b, c):
    """
    ??? Write what needs to be done ???
    """
    if a==b:
        return c
    elif b==c:
        return a
    else:
        return b


# Add these test cases, and remove this placeholder

# 1. Test Cases from the Examples of Problem Statement
# 2. Other Simple Cases
# 3. Corner/Edge Cases
# 4. Large Inputs

# DO NOT TOUCH THE BELOW CODE
class TestextraNumber(unittest.TestCase):

    def test_01(self):
        self.assertEqual(extraNumber(2,3,2),3)

    def test_02(self):
        input_nums = [3, 2, 2]
        output_nums = 3

        self.assertEqual(extraNumber(input_nums[0],input_nums[1],input_nums[2]), output_nums)

    def test_03(self):
        input_nums = [4, 4, 5]
        output_nums = 5

        self.assertEqual(extraNumber(input_nums[0],input_nums[1],input_nums[2]), output_nums)


if __name__ == '__main__':
    unittest.main(verbosity=2)
