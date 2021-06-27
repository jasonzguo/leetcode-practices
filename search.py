"""
统计一个数字在排序数组中出现的次数。

示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2

示例 2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: 0
 
限制：
0 <= 数组长度 <= 50000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
import sure


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if target < nums[m]:
                r = m - 1
            elif target > nums[m]:
                l = m + 1
            else:  # target == nums[m]
                while nums[r] > nums[m]:
                    r -= 1
                while nums[l] < nums[m]:
                    l += 1
                break

        return r - l + 1


solution = Solution()
solution.search([], 8).should.equal(0)
solution.search([5, 5, 5], 5).should.equal(3)
solution.search([5, 7, 7, 8, 8, 10], 8).should.equal(2)
solution.search([5, 7, 7, 8, 8, 10], 6).should.equal(0)
solution.search([1, 2, 3, 3, 3, 3, 4, 5, 9], 3).should.equal(4)
