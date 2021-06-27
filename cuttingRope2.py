"""
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），
每段绳子的长度记为 k[0],k[1]...k[m - 1] 。请问 k[0]*k[1]*...*k[m - 1] 可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：
输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1

示例 2:
输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36

提示：
	2 <= n <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import sure

MAX = 1e9 + 7

def toMod(n: int) -> int:
	if n >= MAX:
		return int(n % MAX)
	return n

class Solution:
	def cuttingRope(self, n: int) -> int:
		if n == 2:
			return 1
		if n == 3:
			return 2

		m = n
		result = 1

		while m > 0:
			if m <= 3:
				result = result * m
				m -= m
			elif (m - 2) * 2 > (m - 3) * 3:
				result = result * 2
				m -= 2
			else:
				result = result * 3
				m -= 3
			result = toMod(result)
		return result




if __name__ == "__main__":
	solution = Solution()
	# solution.cuttingRope(9).should.equal(27)
	# solution.cuttingRope(100).should.equal(703522804)
	# solution.cuttingRope(101).should.equal(55284199)
	solution.cuttingRope(300).should.equal(886041711)
	# solution.cuttingRope(500).should.equal(300460492)