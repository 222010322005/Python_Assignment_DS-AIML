"""
One night you go for a ride on your motorcycle. At 00:00 you start your engine, and the built-in timer automatically 
begins counting the length of your ride, in minutes. Off you go to explore the neighborhood.

When you finally decide to head back, you realize there's a chance the bridges on your route home are up, 
leaving you stranded! Unfortunately, you don't have your watch on you and don't know what time it is. 
All you know thanks to the bike's timer is that n minutes have passed since 00:00.

Using the bike's timer, calculate the current time. Return an answer as the sum of digits that the digital timer
in the format hh:mm would show.

Example1:
Input = 240
Output = 4
Example2:
Input = 1439
Output = 19

"""

import unittest


def lateRide(num):
    """
    ??? Write what needs to be done ???
    """
    a = num//60
    b = num%60
    return(a//10)+(a%10)+(b//10)+(b%10)


# Add these test cases, and remove this placeholder

# 1. Test Cases from the Examples of Problem Statement
# 2. Other Simple Cases
# 3. Corner/Edge Cases
# 4. Large Inputs

# DO NOT TOUCH THE BELOW CODE
class TestlateRide(unittest.TestCase):

    def test_01(self):
        input_nums = 240
        output_nums = 4

        self.assertEqual(lateRide(input_nums), output_nums)

    def test_01(self):
        input_nums = 808
        output_nums = 14

        self.assertEqual(lateRide(input_nums), output_nums)

    def test_01(self):
        input_nums = 1439
        output_nums = 19

        self.assertEqual(lateRide(input_nums), output_nums)


if __name__ == '__main__':
    unittest.main(verbosity=2)
