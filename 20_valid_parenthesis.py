# 20 - Valid Parenthesis

class Solution:
	def isValid(self, s:str) -> bool:
		stack = []
		open = ['(', '{', '[']
		close = [')', '}', ']']

		for bracket in s:
			if bracket in open:
				stack.append(bracket)
			elif bracket in close:
				index = close.index(bracket)
				
				if len(stack) > 0 and open[index] == stack[-1]:
					stack.pop()
				else:
					return False

			if len(stack) == 0:
				return True
			return False
