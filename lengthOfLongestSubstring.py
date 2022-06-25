"""
给定一个字符串 s ，请你找出其中不含有重复字符的最长子串的长度。

示例1:

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
请注意，你的答案必须是 子串 的长度，"pwke"是一个子序列，不是子串。


提示：
0 <= s.length <= 5 * (10**4)
s由英文字母、数字、符号和空格组成

*移动窗口*

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    	s_length = len(s)

    	if s_length <= 1:
    		return s_length

    	char_dict = {}

    	left = 0
    	right = left
    	result = 0

    	while right < s_length:
    		char = s[right]
    		if s[right] not in char_dict:
    			char_dict[char] = right
    		else:
    			result = max(result, right - left)
    			if char_dict[char] <= left:
					char_dict[char] = right
                else:
					left = char_dict[char] + 1
    			    char_dict[char] = right
    		right += 1
    	print(left)
    			

    	return max(result, right - left)

