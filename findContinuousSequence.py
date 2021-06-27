"""
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

示例 1：
输入：target = 9
输出：[[2,3,4],[4,5]]

示例 2：
输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
 
限制：
1 <= target <= 10^5

Lesson:
Sliding Window Algorithm

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
import math
import sure


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        sum = 0
        queue = []
        result = []

        for i in range(1, math.ceil(target / 2) + 1):
            queue.append(i)
            sum += i

            while sum > target:
                sum -= queue.pop(0)

            if sum == target and len(queue) >= 2:
                result.append(queue[:])

        return result


solution = Solution()
solution.findContinuousSequence(1).should.equal([])
solution.findContinuousSequence(2).should.equal([])
solution.findContinuousSequence(3).should.equal([[1, 2]])
solution.findContinuousSequence(9).should.equal([[2, 3, 4], [4, 5]])
solution.findContinuousSequence(15).should.equal(
    [[1, 2, 3, 4, 5], [4, 5, 6], [7, 8]])
