"""
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。
例如，序列 {1,2,3,4,5} 是某栈的压栈序列，序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，
但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。

示例 1：
输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
输出：true
解释：我们可以按以下顺序执行：
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

示例 2：
输入：pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
输出：false
解释：1 不能在 2 之前弹出。

提示：
	0 <= pushed.length == popped.length <= 1000
	0 <= pushed[i], popped[i] < 1000
	pushed 是 popped 的排列。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import sure
from typing import List

class Solution:
	def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
		item_count = len(pushed)

		if item_count <= 1:
			return True

		stack = [pushed[0]]
		pushed_i = 1
		popped_i = 0

		while popped_i < item_count:
			if len(stack) > 0 and stack[-1] == popped[popped_i]:
				stack.pop()
				popped_i += 1
			elif pushed_i < item_count:
				stack.append(pushed[pushed_i])
				pushed_i += 1
			else:
				return False
		return True


solution = Solution()

solution.validateStackSequences([], []).should.equal(True)
solution.validateStackSequences([1], [1]).should.equal(True)
solution.validateStackSequences([2,1,0], [2,0,1]).should.equal(True)
solution.validateStackSequences([1,2,3,4,5], [4,5,3,2,1]).should.equal(True)
solution.validateStackSequences([1,2,3,4,5], [4,3,5,1,2]).should.equal(False)
solution.validateStackSequences([1,0,2], [2,1,0]).should.equal(False)