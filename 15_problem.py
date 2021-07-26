"""
Sum of First N Odd Integers.

### Sample input and output
n = 3 => 1 3 5 => 9  
n = 5 => 1 3 5 7 9 => 25  
n = 6 => 1 3 5 7 9 11 => 36  
 
"""

import unittest


def Program(n):
	count=1
	i=1
	sum=0
	while count <= n:
		sum += i
		i += 2
		count += 1
	#print(sum)
	return sum


# DO NOT TOUCH THE BELOW CODE
class TestProgram(unittest.TestCase):

	def test_01(self): self.assertEqual(Program(3),9)

	def test_02(self): self.assertEqual(Program(5),25)

	def test_03(self): self.assertEqual(Program(6),36)

	def test_04(self): self.assertEqual(Program(7),49)

	def test_05(self): self.assertEqual(Program(8),64)


if __name__ == '__main__':
    unittest.main(verbosity=2)
