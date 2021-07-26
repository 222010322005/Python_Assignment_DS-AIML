"""
Some phone usage rate may be described as follows:

first minute of a call costs min1 cents,
each minute from the 2nd up to 10th (inclusive) costs min2_10 cents
each minute after 10th costs min11 cents.
You have s cents on your account before the call. What is the duration of the longest call (in minutes 
rounded down to the nearest integer) you can have?
Example1:
Input = [2, 2, 1, 2]
Output = 14
Example2:
Input = [10, 1, 2, 22]
Output = 11
"""

import unittest


def phoneCall(min1, min2_10, min11, s):
    """
    ??? Write what needs to be done ???
    """
    if s<min1:
        return 0
    for i in range(2,11):
        if s<min1+min2_10*(i-1):
            return i-1
    return(s-min1-min2_10*9.0)//min11+10


# Add these test cases, and remove this placeholder

# 1. Test Cases from the Examples of Problem Statement
# 2. Other Simple Cases
# 3. Corner/Edge Cases
# 4. Large Inputs

# DO NOT TOUCH THE BELOW CODE
class TestphoneCall(unittest.TestCase):

    def test_01(self):
        input_nums = [3, 1, 2, 20]
        output_num = 14

        self.assertEqual(phoneCall(input_nums[0],input_nums[1],input_nums[2],input_nums[3]), output_num)

    def test_02(self):
        input_nums = [2, 2, 1, 2]
        output_num = 1

        self.assertEqual(phoneCall(input_nums[0],input_nums[1],input_nums[2],input_nums[3]), output_num)

    def test_03(self):
        input_nums = [10, 1, 2, 22]
        output_num = 11

        self.assertEqual(phoneCall(input_nums[0],input_nums[1],input_nums[2],input_nums[3]), output_num)

    def test_04(self):
        input_nums = [2, 2, 1, 24]
        output_num = 14

        self.assertEqual(phoneCall(input_nums[0],input_nums[1],input_nums[2],input_nums[3]), output_num)


if __name__ == '__main__':
    unittest.main(verbosity=2)
