import sure

class Solution:
  maximalSquare(self, matrix):
    return 5

solution = Solution()

solution.maximalSquare([
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]).should.equal(4)