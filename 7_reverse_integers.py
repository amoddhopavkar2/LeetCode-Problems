# 7 - Reverse Integer

class Solution:
	def reverse(self, x: int) -> int:
		lst = str(x)
		reverse = lst[::-1]

		if reverse[-1] == '-':
			rev = reverse[-1] + reverse[:-1]
			reverse = int(rev)
		else:
			reverse = int(reverse)

		if reverse > (-2 ** 31) and reverse < (2 ** 31 - 1):
			return reverse
		return 0
