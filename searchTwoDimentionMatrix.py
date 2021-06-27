"""
  编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：

  每行的元素从左到右升序排列。
  每列的元素从上到下升序排列。
  示例:

  来源：力扣（LeetCode）
  链接：https://leetcode-cn.com/problems/search-a-2d-matrix-ii
  著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from sure import expect


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if (len(matrix) == 0 or len(matrix[0]) == 0):
            return False

        rowIndex = 0
        columnIndex = len(matrix[0]) - 1

        while (rowIndex < len(matrix) and columnIndex >= 0):
            source = matrix[rowIndex][columnIndex]
            if (target == source):
                return True
            elif target < source:
                columnIndex -= 1
            else:
                rowIndex += 1

        return False


solution = Solution()

sampleMatrix = [
    [1,   4,  7, 11, 15],
    [2,   5,  8, 12, 19],
    [3,   6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]

expect(solution.searchMatrix(sampleMatrix, 5)).to.equal(True)
expect(solution.searchMatrix(sampleMatrix, 20)).to.equal(False)
expect(solution.searchMatrix([], 20)).to.equal(False)
