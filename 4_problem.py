"""
n children have got m pieces of candy. They want to eat as much candy as they can, but each child must eat exactly the same amount of candy as any other child.
Determine how many pieces of candy will be eaten by all the children together.Individual pieces of candy cannot be split.
Example 1:
Input = [3, 10]
Output = 9
Example 2:
Input = [9, 100]
Output = 99
"""

import unittest


def candies(num1,num2):
    """
    ??? Write what needs to be done ???
    """
    a = num2%num1
    return num2-a


# Add these test cases, and remove this placeholder

# 1. Test Cases from the Examples of Problem Statement
# 2. Other Simple Cases
# 3. Corner/Edge Cases
# 4. Large Inputs

# DO NOT TOUCH THE BELOW CODE
class Testcandies(unittest.TestCase):

    def test_01(self):
        input_nums = [3, 10]
        output_nums = 9

        self.assertEqual(candies(input_nums[0],input_nums[1]), output_nums)

    def test_02(self):
        input_nums = [10, 5]
        output_nums = 0

        self.assertEqual(candies(input_nums[0],input_nums[1]), output_nums)

    def test_03(self):
        input_nums = [9, 100]
        output_nums = 99

        self.assertEqual(candies(input_nums[0],input_nums[1]), output_nums)


if __name__ == '__main__':
    unittest.main(verbosity=2)
