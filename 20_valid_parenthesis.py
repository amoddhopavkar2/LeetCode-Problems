# 20 - Valid Parenthesis

class Solution:
	def isValid(self, s:str) -> bool:
		stack = []
		open_list = ['(', '{', '[']
		close_list = [')', '}', ']']

		for bracket in s:
			if bracket in open_list:
				stack.append(bracket)
			elif bracket in close_list:
				index = close_list.index(bracket)
				if len(stack) > 0 and open_list[index] == stack[-1]:
					stack.pop()
				else:
					return False
		if len(stack) == 0:
			return True
		return False
