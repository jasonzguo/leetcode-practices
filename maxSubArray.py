"""
输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。
求所有子数组的和的最大值。

要求时间复杂度为O(n)。

示例1:
输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
 
提示：
1 <= arr.length <= 10^5
-100 <= arr[i] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
import sure


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        max_sum = -100

        for i in range(0, len(nums)):
            cur_sum += nums[i]
            if cur_sum > max_sum:
                max_sum = cur_sum
            if cur_sum < 0:
                cur_sum = 0

        return max_sum


solution = Solution()
solution.maxSubArray([-2]).should.equal(-2)
solution.maxSubArray([-2, 1]).should.equal(1)
solution.maxSubArray([-2, 1, -3]).should.equal(1)
solution.maxSubArray([-2, 1, -3, 4]).should.equal(4)
solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]).should.equal(6)
solution.maxSubArray([8, -19, 5, -4, 20]).should.equal(21)
