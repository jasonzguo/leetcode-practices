"""
输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。
比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

示例 1:
输入: n = 1
输出: [1,2,3,4,5,6,7,8,9]

说明：

用返回一个整数列表来代替打印
n 为正整数
"""
from typing import List

import sure


class Solution:
    def printNumbers(self, n: int) -> List[int]:
        max = 10**n
        result = []
        for i in range(1, max):
            result.append(i)
        return result

    def printBigNumbers(self, n: int) -> List[str]:
        pass


solution = Solution()
solution.printNumbers(1).should.equal([1, 2, 3, 4, 5, 6, 7, 8, 9])
solution.printBigNumbers(1).should.equal(
    ["1", "2", "3", "4", "5", "6", "7", "8", "9"])
