"""
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

输入：n = 2
输出：1
示例 2：

输入：n = 5
输出：5

提示：

0 <= n <= 100
"""

import sure

MAX = 1e9+7


class Solution:
    def fib(self, n: int) -> int:
        fib_prev_prev = 0
        fib_prev = 1

        if (n == 0):
            return 0
        if (n == 1):
            return 1

        for i in range(2, n):
            temp = fib_prev
            fib_prev = fib_prev_prev + fib_prev
            if (fib_prev > MAX):
                fib_prev = int(fib_prev % MAX)

            fib_prev_prev = temp

        result = fib_prev_prev + fib_prev

        if (result > MAX):
            return int(result % MAX)
        return result


solution = Solution()
solution.fib(2).should.equal(1)
solution.fib(5).should.equal(5)
solution.fib(14).should.equal(377)
solution.fib(45).should.equal(134903163)
solution.fib(100).should.equal(687995182)
