"""
You found two items in a treasure chest! The first item weighs weight1 and is worth value1,
 and the second item weighs weight2 and is worth value2. What is the total maximum value 
 of the items you can take with you, assuming that your max weight capacity is maxW and 
 you can't come back for the items later?
Note that there are only two items and you can't bring more than one item of each type,
i.e. you can't take two first items or two second items.


Example1:
Input = [10, 5, 6, 4, 8]
Output = 10
Example2:
Input = [10, 5, 6, 4, 9]
Output = 16
"""

import unittest


def knapsackLight(value1, weight1, value2, weight2, maxW):
    """
    ??? Write what needs to be done ???
    """
    if (maxW >= weight1+weight2):
        return value1+value2
    elif (value1>value2 and maxW >= weight1):
        return value1
    elif (value1<value2 and maxW >= weight2):
        return value2
    elif (maxW >= weight1):
        return value1
    elif (maxW >= weight1):
        return value1
    else:
        return 0


# Add these test cases, and remove this placeholder

# 1. Test Cases from the Examples of Problem Statement
# 2. Other Simple Cases
# 3. Corner/Edge Cases
# 4. Large Inputs

# DO NOT TOUCH THE BELOW CODE
class TestknapsackLight(unittest.TestCase):

    def test_01(self):
        input_nums = [10, 5, 6, 4, 8]
        output_nums = 10

        self.assertEqual(knapsackLight(input_nums[0],input_nums[1],input_nums[2],input_nums[3],input_nums[4]), output_nums)

    def test_02(self):
        input_nums = [10, 5, 6, 4, 9]
        output_nums = 16

        self.assertEqual(knapsackLight(input_nums[0],input_nums[1],input_nums[2],input_nums[3],input_nums[4]), output_nums)

    def test_03(self):
        input_nums = [5, 3, 7, 4, 6]
        output_nums = 7

        self.assertEqual(knapsackLight(input_nums[0],input_nums[1],input_nums[2],input_nums[3],input_nums[4]), output_nums)


if __name__ == '__main__':
    unittest.main(verbosity=2)
