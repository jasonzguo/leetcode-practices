"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import sure


class Solution:
    def numWays(self, n: int) -> int:
        if (n < 2):
            return 1

        dp = [1, 1]
        for _ in range(2, n + 1):
            temp = dp[0] + dp[1]
            dp[0] = dp[1]
            dp[1] = temp

        return dp[1]


solution = Solution()
solution.numWays(7).should.be.equal(21)
