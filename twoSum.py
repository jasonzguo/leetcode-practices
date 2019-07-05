import sure
"""
    Problem:
        Two Sum
    
    Lessons learned:
        - should pay attention to requirements if it's not clear, think twice
            for example, are all the input numbers positive integers?
        - using dict as a in memory cache
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []

        if len(nums) > 1:
            diff_dict = {}
            for index, num in enumerate(nums):
                diff = str(target - num)
                if diff in diff_dict:
                    result = [diff_dict[diff], index]
                    break
                else:
                    diff_dict[str(num)] = index
        return result


solution = Solution()
solution.twoSum([], 1).should.equal([])
solution.twoSum([1], 2).should.equal([])
solution.twoSum([1, 2], 3).should.equal([0, 1])
solution.twoSum([1, 2, 3], 4).should.equal([0, 2])
solution.twoSum([1, 2, 1], 2).should.equal([0, 2])
# 1st submission failed
solution.twoSum([0, 4, 3, 0], 0).should.equal([0, 3])
# 2nd submission failed
solution.twoSum([-3, 4, 3, 90], 0).should.equal([0, 2])

print('ok')
