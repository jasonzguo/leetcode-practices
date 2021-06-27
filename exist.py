"""
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。
如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，
其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例 1：
输入：
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 
    word = "ABCCED"
输出：true

示例 2：
输入：
    board = [["a","b"],["c","d"]],
    word = "abcd"
输出：false

提示：
1 <= board.length <= 200
1 <= board[i].length <= 200
board 和 word 仅由大小写英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def dfs(self, board, word, i, j, l) -> bool:
        rows_count = len(board)
        columns_count = len(board[0])
        letters_count = len(word)

        # found all letters of the word
        l += 1
        if l == letters_count:
            return True

        board[i][j] = board[i][j] + '#'

        top = (i - 1 >= 0
               and board[i - 1][j] == word[l]
               and self.dfs(board, word, i - 1, j, l))
        if top == True:
            return True

        bottom = (i + 1 < rows_count
                  and board[i + 1][j] == word[l]
                  and self.dfs(board, word, i + 1, j, l))
        if bottom == True:
            return True

        left = (j - 1 >= 0
                and board[i][j - 1] == word[l]
                and self.dfs(board, word, i, j - 1, l))
        if left == True:
            return True

        right = (j + 1 < columns_count
                 and board[i][j + 1] == word[l]
                 and self.dfs(board, word, i, j + 1, l))
        if right == True:
            return True

        # back track
        board[i][j] = str(board[i][j][0])
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        rows_count = len(board)
        columns_count = len(board[0])

        if len(word) > rows_count * columns_count:
            return False

        for i in range(0, rows_count):
            for j in range(0, columns_count):
                if (board[i][j] == word[0]
                        and self.dfs(board, word, i, j, 0) == True):
                    return True
        return False


solution = Solution()

board = [["a", "a", "a", "a"], ["a", "a", "a", "a"], ["a", "a", "a", "a"]]
word = "aaaaaaaaaaaaa"
print(solution.exist(board, word))
