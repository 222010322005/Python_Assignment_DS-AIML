"""
#Check Palindrome

Given a string s, return whether it is a palindrome.

#Constraints

n ≤ 100,000 where n is the length of s

### Sample input and output

s = "racecar"  => True    
s = "evilolive"  => True    
s = "palindrome"  => False  
"""

import unittest


def Palindrome(s):
	s1 = (s)
	flag=True
	for i in range(len(s1)):
		#print(s1[i]+" "+s1[-i-1])
		if s1[i]!=s1[-i-1]:
			flag=False;
	return flag


# Add these test cases, and remove this placeholder

# 1. Test Cases from the Examples of Problem Statement
# 2. Other Simple Cases
# 3. Corner/Edge Cases
# 4. Large Inputs

# DO NOT TOUCH THE BELOW CODE
class TestextraNumber(unittest.TestCase):

	def test_01(self): self.assertEqual(Palindrome("racecar"),True)

	def test_02(self): self.assertEqual(Palindrome("evilolive"),True)

	def test_03(self): self.assertEqual(Palindrome("palindrome"),False)

	def test_04(self): self.assertEqual(Palindrome("madam"),True)

	def test_05(self): self.assertEqual(Palindrome("vikatakiv"),True)


if __name__ == '__main__':
    unittest.main(verbosity=2)
