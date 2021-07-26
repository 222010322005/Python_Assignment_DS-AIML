"""
You are playing an RPG game. Currently your experience points (XP) total is equal to experience. 
To reach the next level your XP should be at least at threshold. If you kill the monster in front of you, 
you will gain more experience points in the amount of the reward.

Given values experience, threshold and reward, check if you reach the next level after killing the monster.
Example1:
Input = [10,15,5]
Output = True
Example2:
Input = [10,15,4]
Output = False
"""

import unittest


def reachNextLevel(experience, threshold, reward):
    """
    ??? Write what needs to be done ???
    """
    if experience+ reward>=threshold:
        return True
    else:
        return False


# Add these test cases, and remove this placeholder

# 1. Test Cases from the Examples of Problem Statement
# 2. Other Simple Cases
# 3. Corner/Edge Cases
# 4. Large Inputs

# DO NOT TOUCH THE BELOW CODE
class TestreachNextLevel(unittest.TestCase):

    def test_01(self):
        input_nums = [10, 15, 5]
        output = True

        self.assertEqual(reachNextLevel(input_nums[0],input_nums[1],input_nums[2]), output)

    def test_02(self):
        input_nums = [10, 15, 4]
        output = False

        self.assertEqual(reachNextLevel(input_nums[0],input_nums[1],input_nums[2]), output)

    def test_03(self):
        input_nums = [3, 6, 4]
        output = True

        self.assertEqual(reachNextLevel(input_nums[0],input_nums[1],input_nums[2]), output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
