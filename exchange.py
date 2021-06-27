"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。

示例：
输入：nums = [1,2,3,4]
输出：[1,3,2,4] 
注：[3,1,2,4] 也是正确的答案之一。
 
提示：
0 <= nums.length <= 50000
1 <= nums[i] <= 10000
"""

from typing import List
import sure


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        odd_list = []
        even_list = []

        for num in nums:
            if num % 2 == 0:
                even_list.append(num)
            else:
                odd_list.append(num)

        return odd_list + even_list

    def exchangeDoublePointers(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        nums_clone = nums[:]

        while left < right:
            left_value = nums[left]
            right_value = nums[right]
            if left_value % 2 == 0 and right_value % 2 == 1:
                nums_clone[left], nums_clone[right] = nums_clone[right], nums_clone[left]
                left += 1
                right -= 1
            elif left_value % 2 == 1:
                left += 1
            elif right_value % 2 == 0:
                right -= 1
        return nums_clone


solution = Solution()
solution.exchangeDoublePointers([1, 2, 3, 4]).should.equal([1, 3, 2, 4])
solution.exchangeDoublePointers([2, 1]).should.equal([1, 2])
solution.exchangeDoublePointers([1]).should.equal([1])
