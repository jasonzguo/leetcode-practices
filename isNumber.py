"""
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。

数值（按顺序）可以分成以下几个部分：
	若干空格
	一个 小数 或者 整数
	（可选）一个 'e' 或 'E' ，后面跟着一个 整数
	若干空格

小数（按顺序）可以分成以下几个部分：
	（可选）一个符号字符（'+' 或 '-'）
	下述格式之一：
		至少一位数字，后面跟着一个点 '.'
		至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
		一个点 '.' ，后面跟着至少一位数字

整数（按顺序）可以分成以下几个部分：
	（可选）一个符号字符（'+' 或 '-'）
	至少一位数字

部分数值列举如下：
	["+100", "5e2", "-123", "3.1416", "-1E-16", "0123"]

部分非数值列举如下：
	["12e", "1a3.14", "1.2.3", "+-5", "12e+5.4"]

示例 1：
输入：s = "0"
输出：true

示例 2：
输入：s = "e"
输出：false

示例 3：
输入：s = "."
输出：false

示例 4：
输入：s = "    .1  "
输出：true

提示：
	1 <= s.length <= 20
	s 仅含英文字母（大写和小写），数字（0-9），加号 '+' ，减号 '-' ，空格 ' ' 或者点 '.' 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import sure

NUMS_DICT = {
	"0": True,
	"1": True,
	"2": True,
	"3": True,
	"4": True,
	"5": True,
	"6": True,
	"7": True,
	"8": True,
	"9": True
}

STATES = {
	"0": {
		"space": "0",
		"sign": "1",
		"digit": "2",
		"dot": "3"
	},
	"1": {
		"digit": "2",
		"dot": "3"
	},
	"2": { # integer
		"digit": "2",
		"dot": "4",
		"e": "5",
		"space": "8"
	},
	"3": {
		"digit": "4"
	},
	"4": { #float
		"digit": "4",
		"e": "5",
		"space": "8"
	},
	"5": {
		"sign": "6",
		"digit": "7"		
	},
	"6": {
		"digit": "7"
	},
	"7": { # scientific
		"digit": "7",
		"space": "8"
	},
	"8": { # end with space
		"space": "8"
	}
}

def is_dot(s: str) -> bool:
	return s == "."

def is_e(s: str) -> bool:
	return s == "e" or s == "E"

def is_digit(s: str) -> bool:
	return s in NUMS_DICT

def is_sign(s: str) -> bool:
	return s == "+" or s == "-"

def is_space(s: str) -> bool:
	return s == " "


class Solution:
	def isNumber(self, s: str) -> bool:
		current_state = STATES["0"]

		for c in s:
			if is_dot(c):
				if "dot" in current_state:
					current_state = STATES[current_state["dot"]]
				else:
					return False
			elif is_e(c):
				if "e" in current_state:
					current_state = STATES[current_state["e"]]
				else:
					return False
			elif is_digit(c):
				if "digit" in current_state:
					current_state = STATES[current_state["digit"]]
				else:
					return False
			elif is_sign(c):
				if "sign" in current_state:
					current_state = STATES[current_state["sign"]]
				else:
					return False
			elif is_space(c):
				if "space" in current_state:
					current_state = STATES[current_state["space"]]
				else:
					return False
			else:
				return False

		return current_state in [STATES["2"], STATES["4"], STATES["7"], STATES["8"]]



if __name__ == '__main__':
	solution = Solution()
	solution.isNumber("0").should.equal(True)
	solution.isNumber("e").should.equal(False)
	solution.isNumber(".").should.equal(False)
	solution.isNumber("  .1  ").should.equal(True)
	solution.isNumber("  1.  ").should.equal(True)

	solution.isNumber("+100").should.equal(True)
	solution.isNumber("5e2").should.equal(True)
	solution.isNumber("3.1416").should.equal(True)
	solution.isNumber("-1E-16").should.equal(True)
	solution.isNumber("0123").should.equal(True)

	solution.isNumber("12e").should.equal(False)
	solution.isNumber("1a3.14").should.equal(False)
	solution.isNumber("3.1.4").should.equal(False)
	solution.isNumber("+-5").should.equal(False)
	solution.isNumber("12e+5.4").should.equal(False)

	solution.isNumber("  ").should.equal(False)
	solution.isNumber(" . ").should.equal(False)
	solution.isNumber(" e9 ").should.equal(False)
	solution.isNumber("e9").should.equal(False)