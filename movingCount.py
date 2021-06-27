"""
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 
一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上
下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。
但它不能进入方格 [35, 38]，因为3+5+3+8=19,
请问该机器人能够到达多少个格子？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


import sure


class Solution:
    def addIndices(self, index_a: int, index_b: int):
        index_a_sum = index_a % 10
        if (index_a > 10):
            index_a_sum += int(index_a / 10)

        index_b_sum = index_b % 10
        if (index_b > 10):
            index_b_sum += int(index_b / 10)

        return index_a_sum + index_b_sum

    def movingCount(self, m: int, n: int, k: int):
        if k == 0:
            return 1

        result = 0
        for mi in range(0, m):
            for ni in range(0, n):
                if (self.addIndices(mi, ni) <= k):
                    top_indices_sum = 0
                    if (mi + 1 < m):
                        top_indices_sum = self.addIndices(mi + 1, ni)

                    bottom_indices_sum = 0
                    if (mi - 1 >= 0):
                        bottom_indices_sum = self.addIndices(mi - 1, ni)

                    right_indices_sum = 0
                    if (ni + 1 < n):
                        right_indices_sum = self.addIndices(mi, ni + 1)

                    left_indices_sum = 0
                    if (ni - 1 >= 0):
                        left_indices_sum = self.addIndices(mi, ni - 1)

                    if top_indices_sum <= k or bottom_indices_sum <= k or right_indices_sum <= k or left_indices_sum <= k:
                        result += 1
        return result


solution = Solution()

solution.movingCount(2, 3, 1).should.be.equal(3)
#solution.movingCount(3, 1, 0).should.be.equal(1)
