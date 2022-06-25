"""
	https://leetcode.com/problems/longest-common-prefix/

	Constraints:
    	1 <= strs.length <= 200
    	0 <= strs[i].length <= 200
    	strs[i] consists of only lower-case English letters.
"""

import sure
from typing import List

class Solution:
	def longestCommonPrefix(self, strs: List[str]) -> str:
		if len(strs) == 1:
			return strs[0]

		result = ""

		i = 0
		first_str = strs[0]
		while i < len(first_str):
			j = 1

			while j < len(strs):
				other_str = strs[j]
				if i > len(other_str) - 1:
					return result
				elif first_str[i] != other_str[i]:
					return result

				if j == len(strs) - 1:
					result += first_str[i]
				j += 1
			i += 1


		return result


solution = Solution()
solution.longestCommonPrefix(["flower"]).should.equal("flower")
solution.longestCommonPrefix(["flower","flow","flight"]).should.equal("fl")
solution.longestCommonPrefix(["dog","racecar","car"]).should.equal("")
