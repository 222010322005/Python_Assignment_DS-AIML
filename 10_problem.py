"""
In tennis, the winner of a set is based on how many games each player wins. The first player to win 6 games is 
declared the winner unless their opponent had already won 5 games, in which case the set continues until one of 
the players has won 7 games.
Given two integers score1 and score2, your task is to determine if it is possible for a tennis set to be finished with a final score of score1 : score2.
Example 1:
Input = [3,6]
Output = True
Example 2:
Input = [6,5]
Output = False
"""

import unittest


def tennisSet(score1, score2):
    """
    ??? Write what needs to be done ???
    """
    if (score1== 6 or score2==6) and (score1 <=4 or score2 <=4):
        return True
    elif (score1==7 and (score2 ==5 or score2 == 6)):
        return True
    elif (score2==7 and (score1 ==5 or score1 == 6)):
        return True
    else:
        return False


# Add these test cases, and remove this placeholder

# 1. Test Cases from the Examples of Problem Statement
# 2. Other Simple Cases
# 3. Corner/Edge Cases
# 4. Large Inputs

# DO NOT TOUCH THE BELOW CODE
class TesttennisSet(unittest.TestCase):

    def test_01(self):
        input_nums = [3, 6]
        output = True

        self.assertEqual(tennisSet(input_nums[0],input_nums[1]), output)

    def test_02(self):
        input_nums = [6, 5]
        output = False

        self.assertEqual(tennisSet(input_nums[0],input_nums[1]), output)

    def test_03(self):
        input_nums = [6, 4]
        output = True

        self.assertEqual(tennisSet(input_nums[0],input_nums[1]), output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
