"""
请实现一个函数，把字符串 s 中的每个空格替换成"%20"

示例 1：

输入：s = "We are happy."
输出："We%20are%20happy."

限制：

0 <= s 的长度 <= 10000
"""

import sure


class Solution:
    def replaceSpace(self, s: str) -> str:
        if len(s) == 0:
            return s

        result = ""

        for char in s:
            if char == ' ':
                result += "%20"
            else:
                result += char
        return result


solution = Solution()
solution.replaceSpace("").should.equal("")
solution.replaceSpace("  ").should.equal("%20%20")
solution.replaceSpace("We.").should.equal("We.")
solution.replaceSpace("We are happy.").should.equal("We%20are%20happy.")
