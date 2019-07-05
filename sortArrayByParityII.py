"""
    Problem:
        Sort Array By Parity II:
            Sort the array so that whenever A[i] is odd, 
            i is odd; and whenever A[i] is even, i is even.

    Lessons Learned:
        - thinking of past experiences
        - there could be more optimal solutions
"""

import sure


class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        result = [0] * len(A)
        even_index = 0
        odd_index = 1
        for num in A:
            if num % 2 == 0:
                result[even_index] = num
                even_index += 2
            else:
                result[odd_index] = num
                odd_index += 2
        return result

    def sortArrayByParityII_inplace(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd_index = 1
        for even_index in range(0, len(A), 2):
            if A[even_index] % 2 == 0:
                continue
            while A[odd_index] % 2 == 1:
                odd_index += 2
            A[even_index], A[odd_index] = A[odd_index], A[even_index]
        return A


solution = Solution()
solution.sortArrayByParityII([2, 1]).should.equal([2, 1])
solution.sortArrayByParityII([1, 2]).should.equal([2, 1])
solution.sortArrayByParityII([2, 4, 1, 3]).should.equal([2, 1, 4, 3])
solution.sortArrayByParityII([1, 3, 2, 4]).should.equal([2, 1, 4, 3])
solution.sortArrayByParityII([1, 2, 3, 4]).should.equal([2, 1, 4, 3])
solution.sortArrayByParityII([1, 2, 4, 3]).should.equal([2, 1, 4, 3])

solution.sortArrayByParityII_inplace([2, 1]).should.equal([2, 1])
solution.sortArrayByParityII_inplace([1, 2]).should.equal([2, 1])
solution.sortArrayByParityII_inplace([2, 4, 1, 3]).should.equal([2, 1, 4, 3])
solution.sortArrayByParityII_inplace([1, 3, 2, 4]).should.equal([4, 3, 2, 1])
solution.sortArrayByParityII_inplace([1, 2, 3, 4]).should.equal([2, 1, 4, 3])
solution.sortArrayByParityII_inplace([1, 2, 4, 3]).should.equal([2, 1, 4, 3])

print('ok')