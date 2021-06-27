"""
给你一个字符串 s，由若干单词组成，单词之间用空格隔开。
返回字符串中最后一个单词的长度。如果不存在最后一个单词，请返回 0 。

单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。

示例 1：
输入：s = "Hello World"
输出：5

示例 2：
输入：s = " "
输出：0
 

提示：
1 <= s.length <= 104
s 仅有英文字母和空格 ' ' 组成
"""
import sure


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = 0

        for i in range(0, len(s)):
            j = i - 1
            c = s[i]

            if c != ' ':
                if j >= 0 and s[j] == ' ':
                    result = 1
                else:
                    result += 1
        return result

    def lengthOfLastWordOfficial(self, s: str) -> int:
        end = len(s) - 1

        while (end >= 0) and (s[end] == ' '):
            end -= 1

        if end < 0:
            return 0

        start = end

        while (start >= 0) and (s[start] != ' '):
            start -= 1

        return end - start


solution = Solution()
solution.lengthOfLastWordOfficial("Hell o  ").should.equal(1)
solution.lengthOfLastWordOfficial("Hello World").should.equal(5)
solution.lengthOfLastWordOfficial("Hello Worldi ").should.equal(6)
solution.lengthOfLastWordOfficial(" ").should.equal(0)
