"""
Consider an arithmetic expression of the form a#b=c. Check whether it is possible to replace # with one of the 
four signs: +, -, * or / to obtain a correct expression.
Example 1:
Input = [2,3,5]
Output = True
Example 2:
Input = [8,3,2]
Output = False
"""

import unittest


def arithmeticExpression(a,b,c):
    """
    ??? Write what needs to be done ???
    """
    if a + b == c:
        return True
    elif a - b == c:
        return True
    elif a * b == c:
        return True
    elif a / b == c:
        return True
    else:
        return False


# Add these test cases, and remove this placeholder

# 1. Test Cases from the Examples of Problem Statement
# 2. Other Simple Cases
# 3. Corner/Edge Cases
# 4. Large Inputs

# DO NOT TOUCH THE BELOW CODE
class TestarithmeticExpression(unittest.TestCase):

    def test_01(self):
        input_nums = [2, 3, 5]
        output = True

        self.assertEqual(arithmeticExpression(input_nums[0],input_nums[1],input_nums[2]), output)
    
    def test_02(self):
        input_nums = [8, 3, 2]
        output = False

        self.assertEqual(arithmeticExpression(input_nums[0],input_nums[1],input_nums[2]), output)

    def test_03(self):
        input_nums = [6, 3, 3]
        output = True

        self.assertEqual(arithmeticExpression(input_nums[0],input_nums[1],input_nums[2]), output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
