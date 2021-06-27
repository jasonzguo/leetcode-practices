from typing import List
import sure


class Solution:
    def solve(self, nums, left, right):
        if left >= right:
            return (left, right)

        mid = (left + right) // 2

        left_sub = self.solve(nums, left, mid)
        right_sub = self.solve(nums, mid + 1, right)

        left_sum = 0
        for i in range(left_sub[0], left_sub[1] + 1):
            left_sum += nums[i]
        right_sum = 0
        for i in range(right_sub[0], right_sub[1] + 1):
            right_sum += nums[i]

        mid_sum = 0
        mid_max_sum = 0
        mid_right = left_sub[0]
        for i in range(left_sub[0], right_sub[1] + 1):
            mid_sum += nums[i]
            if mid_sum > mid_max_sum:
                mid_max_sum = mid_sum
                mid_right = i

        if left_sum >= right_sum and left_sum >= mid_max_sum:
            return left_sub
        if right_sum >= left_sum and right_sum >= mid_max_sum:
            return right_sub
        if mid_max_sum >= left_sum and mid_max_sum >= right_sum:
            return (left_sub[0], mid_right)

    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = self.solve(nums, 0, len(nums) - 1)
        print(max_sub)
        max_sum = 0
        for i in range(max_sub[0], max_sub[1] + 1):
            max_sum += nums[i]
        return max_sum


solution = Solution()
solution.maxSubArray([8, -19, 5, -4, 20]).should.equal(21)
