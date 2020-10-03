# 20 - Valid Parenthesis

class Solution:
	def isValid(self, s:str) -> bool:
		stack = []
		open_lst = ['(', '{', '[']
		close_lst = [')', '}', ']']

		for bracket in s:
			if bracket in open_lst:
				stack.append(bracket)
			elif bracket in close_lst:
				index = close_lst.index(bracket)
				
				if len(stack) > 0 and open_lst[index] == stack[-1]:
					stack.pop()
				else:
					return False

			if len(stack) == 0:
				return True
			return False
