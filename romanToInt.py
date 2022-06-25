"""
	https://leetcode.com/problems/roman-to-integer/
"""

import sure

LETTER_TO_INT_MAP = {
	'I': 1,
	'V': 5,
	'X': 10,
	'L': 50,
	'C': 100,
	'D': 500,
	'M': 1000
}

class Solution:
	def romanToInt(self, s: str) -> int:
		result = 0

		for i, c in enumerate(s):
			val = LETTER_TO_INT_MAP[c]
			if i+1 < len(s) and LETTER_TO_INT_MAP[s[i+1]] > val:
				result -= val
			else:
				result += val
		return result


solution = Solution()
solution.romanToInt("III").should.equal(3)
solution.romanToInt("IV").should.equal(4)
solution.romanToInt("XL").should.equal(40)
solution.romanToInt("XC").should.equal(90)
solution.romanToInt("CD").should.equal(400)
solution.romanToInt("CM").should.equal(900)
solution.romanToInt("LVIII").should.equal(58)
solution.romanToInt("MCMXCIV").should.equal(1994)