"""
	https://leetcode.com/problems/valid-parentheses/

	Constraints:
    	1 <= s.length <= 104
   		s consists of parentheses only '()[]{}'.
"""

import sure

OPEN_TO_CLOSE_MAP = {
	'(': ')',
	'[': ']',
	'{': '}'
}

class Solution:
	def isValid(self, s: str) -> bool:
		result = False

		if len(s) % 2 == 1:
			return result

		open_stack = []
		pairs_to_find = len(s) / 2

		for c in s:
			if c == "(" or c == '[' or c == '{':
				open_stack.append(c)
			elif len(open_stack) > 0 and c == OPEN_TO_CLOSE_MAP[open_stack[-1]]:
				open_stack.pop()
				pairs_to_find -= 1
			else:
				break

		if pairs_to_find == 0:
			result = True
		return result

solution = Solution()
solution.isValid("()").should.equal(True)
solution.isValid("([][])").should.equal(True)
solution.isValid("([[]])").should.equal(True)
solution.isValid("([[]])[}").should.equal(False)
solution.isValid("([])([])").should.equal(True)
solution.isValid("()[]{}").should.equal(True)
solution.isValid("(]").should.equal(False)
solution.isValid("([)]").should.equal(False)
