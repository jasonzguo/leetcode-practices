"""
从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。
2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。
A 不能视为 14。

示例 1:
输入: [1,2,3,4,5]
输出: True

示例 2:
输入: [0,0,1,2,5]
输出: True

限制：
数组长度为 5 
数组的数取值为 [0, 13]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
import sure


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        visited = [0] * 14
        max_num = 0

        for num in nums:
            # non-zero duplicate
            if num != 0 and visited[num] == 1:
                return False

            visited[num] += 1
            max_num = max(max_num, num)

        if max_num > 5:
            for i in range(1, 5):
                if visited[max_num - i] == 0 and visited[0] == 0:
                    return False
                if visited[max_num - i] == 0:
                    visited[0] -= 1
        return True


solution = Solution()
solution.isStraight([2, 3, 1, 5, 4]).should.equal(True)
solution.isStraight([1, 2, 3, 4, 5]).should.equal(True)
solution.isStraight([0, 0, 1, 2, 5]).should.equal(True)
solution.isStraight([0, 0, 0, 0, 0]).should.equal(True)
solution.isStraight([10, 11, 12, 13, 0]).should.equal(True)
solution.isStraight([2, 4, 5, 7, 0]).should.equal(False)
solution.isStraight([2, 4, 0, 7, 0]).should.equal(False)
solution.isStraight([2, 4, 0, 5, 0]).should.equal(False)
