"""
输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。
为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student. "，
则输出"student. a am I"。

 
示例 1：
输入: "the sky is blue"
输出: "blue is sky the"

示例 2：
输入: "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。

示例 3：
输入: "a good   example"
输出: "example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
 
说明：
无空格字符构成一个单词。
输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import sure


class Solution:
    def strip(self, s: str) -> str:
        i = 1
        j = len(s) - 2

        while i < j:
            if s[i] == s[i-1] == ' ':
                i += 1
            elif s[j] == s[j + 1] == ' ':
                j -= 1
            else:
                return s[i-1:j+2]
        return " "

    def reverseWords(self, s: str) -> str:
        start = 0
        end = len(s) - 1

        i = start
        j = end

        prefix = ""
        suffix = ""

        while i < j:
            if s[i] != ' ':
                i += 1

            while s[start] == ' ':
                start += 1
                i += 1

            if s[j] != ' ':
                j -= 1

            while s[end] == ' ':
                end -= 1
                j -= 1

            if i == j:
                break

            if s[i] == s[j] == ' ':
                word_one = s[start:i]

                original_other_words = s[i:j+1]
                other_words = self.strip(original_other_words)

                word_two = s[j+1:end+1]

                s = prefix + word_two + other_words + word_one + suffix

                prefix = prefix + word_two + ' '
                suffix = ' ' + word_one + suffix
                start += + len(word_two) + 1
                end -= len(word_one) + 1 + \
                    (len(original_other_words) - len(other_words))
                i = start
                j = end
        return s


solution = Solution()
# solution.reverseWords("  hello ").should.equal("hello")
solution.reverseWords("  hello world!  ").should.equal("world! hello")
# solution.reverseWords("hello  world!").should.equal("world! hello")
# solution.reverseWords("a good   example").should.equal("example good a")
# solution.reverseWords("the sky is blue").should.equal("blue is sky the")
# solution.reverseWords("one two three four five six seven").should.equal(
#     "seven six five four three two one")
# solution.reverseWords(
#     "  Bob    Loves  Alice   ").should.equal("Alice Loves Bob")
# solution.reverseWords(
#     "Alice does not even like bob").should.equal("bob like even not does Alice")
