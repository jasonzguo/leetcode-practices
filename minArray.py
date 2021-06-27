"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。

示例 1：
输入：[3,4,5,1,2]
输出：1

示例 2：
输入：[2,2,2,0,1]
输出：0

提示：

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
nums 原来是一个升序排序的数组，并进行了 1 至 n 次旋转

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List

import sure

import math


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        numbers_count = len(numbers)

        if numbers_count == 1:
            return numbers[0]

        i = 0
        j = 1
        while j < numbers_count:
            if numbers[i] > numbers[j]:
                break
            i += 1
            j += 1
        return numbers[j]

    def minArrayBinary(self, numbers: List[int]) -> int:
        numbers_count = len(numbers)

        if numbers_count == 1:
            return numbers[0]

        l = 0
        r = numbers_count - 1

        while l < r:
            m = math.floor((l+r) / 2)
            l_value = numbers[l]
            r_value = numbers[r]
            m_value = numbers[m]

            if l_value < r_value:
                return l_value

            if r_value < m_value:
                l = m + 1
            elif l_value < m_value:
                r = m - 1
            else:
                r -= 1
        return numbers[l]


solution = Solution()
solution.minArrayBinary([3, 4, 5, 1, 2]).should.equal(1)
solution.minArrayBinary([2, 2, 2, 0, 1]).should.equal(0)

# [1,2,3,4,5]
# [5,1,2,3,4]
# [4,5,1,2,3]
# [3,4,5,1,2]
# [2,3,4,5,1]

# [0,1,2,2,2]
# [2,0,1,2,2]
# [2,2,0,1,2]
# [2,2,2,0,1]
