"""
输入一个字符串，打印出该字符串中字符的所有排列。
你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

示例:
输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]

限制：
1 <= s 的长度 <= 8

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import sure
from typing import List

def factorial(n: int) -> int:
	if n <= 1:
		return 1

	result = 1
	for i in range(2, n + 1):
		result *= i
	return result

class Solution:
	def get_rest(self, i, s):
		new_s = ""
		for j in range(0, len(s)):
			if i != j:
				new_s += s[j]
		return new_s

	def solve(self, s):
		s_length = len(s)
		if s_length == 1:
			return [s]
		if s_length == 2:
			if s[0] == s[1]:
				return [s]
			else:
				return [s[0] + s[1], s[1] + s[0]]

		result = []

		visited = {}
		for i in range(0, s_length):
			if s[i] in visited:
				continue
			r = self.solve(self.get_rest(i, s))
			r = [s[i] + x for x in r]
			result += r
			visited[s[i]] = True
		return result

	def permutation(self, s: str) -> List[str]:
		s_length = len(s)
		return self.solve(s)


solution = Solution()

# result = solution.permutation("ab")
# result.should.equal(["ab", "ba"])
# len(result).should.equal(factorial(2))

# result = solution.permutation("abc")
# result.should.equal(["abc","acb","bac","bca","cab","cba"])
# len(result).should.equal(factorial(3))

# result = solution.permutation("abcd")
# result.should.equal(["abcd","abdc","acbd","acdb","adbc","adcb",
# 	"bacd","badc","bcad","bcda","bdac","bdca","cabd",
# 	"cadb","cbad","cbda","cdab","cdba",
# 	"dabc","dacb","dbac","dbca","dcab","dcba"])
# len(result).should.equal(factorial(4))

result = solution.permutation("aab")
result.should.equal(["aba","aab","baa"])