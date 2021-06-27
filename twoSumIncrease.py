"""
输入一个递增排序的数组和一个数字s，在数组中查找两个数，
使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。

示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]

示例 2：
输入：nums = [10,26,30,31,47,60], target = 40
输出：[10,30] 或者 [30,10]
 
限制：
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import sure
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []

        nums_count = len(nums)

        l = 0
        r = nums_count - 1

        while l < r:
            m = (l + r) // 2

            if nums[l] + nums[r] == target:
                result.append(nums[l])
                result.append(nums[r])
                return result

            if nums[m] >= target:
                r = m - 1
            elif nums[l] + nums[m] > target:
                r = m - 1
            elif nums[r] + nums[m] < target:
                l = m + 1
            elif nums[l] + nums[r] > target:
                r -= 1
            elif nums[l] + nums[r] < target:
                l += 1

        return result


solution = Solution()
solution.twoSum([9], 9).should.equal([])
solution.twoSum([2, 7, 11, 15], 9).should.equal([2, 7])
solution.twoSum([10, 26, 30, 31, 47, 60], 400).should.equal([])
solution.twoSum([10, 26, 30, 31, 47, 60], 40).should.equal([10, 30])
solution.twoSum([10, 26, 30, 31, 47, 60], 5).should.equal([])
solution.twoSum([10, 26, 30, 31, 47, 60], 45).should.equal([])
