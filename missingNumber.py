"""
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。
在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

示例 1:
输入: [0,1,3]
输出: 2

示例 2:
输入: [0,1,2,3,4,5,6,7,9]
输出: 8
 
限制：
1 <= 数组长度 <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/que-shi-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
import sure


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0

        for i in range(0, len(nums)):
            if nums[i] != i:
                return i
            i += 1

        return i

    def missingNumberBinary(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if m != nums[m]:
                r = m - 1
            else:  # m == nums[m]
                l = m + 1

        return l


solution = Solution()
solution.missingNumberBinary([0, 1]).should.equal(2)
solution.missingNumberBinary([0]).should.equal(1)
solution.missingNumberBinary([0, 1, 3]).should.equal(2)
solution.missingNumberBinary([0, 1, 2, 3, 4, 5, 6, 7, 9]).should.equal(8)
solution.missingNumberBinary([1, 2, 3]).should.equal(0)
