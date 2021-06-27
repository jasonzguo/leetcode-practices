"""
输入整数数组 arr ，找出其中最小的 k 个数。
例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

示例 1：
输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]

示例 2：
输入：arr = [0,1,2,1], k = 1
输出：[0]

限制：
0 <= k <= arr.length <= 10000
0 <= arr[i] <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List
import sure
import math


class Solution:
    def mergeSort(self, arr):
        if len(arr) > 1:

            m = len(arr) // 2
            left = arr[:m]
            right = arr[m:]

            self.mergeSort(left)
            self.mergeSort(right)

            i = j = k = 0

            while (i < len(left)) and (j < len(right)):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        self.mergeSort(arr)
        return arr[0:k]


solution = Solution()
solution.getLeastNumbers([3, 2, 1], 2).should.equal([1, 2])
solution.getLeastNumbers([0, 1, 2, 1], 1).should.equal([0])
