# 38 - Count and Say

class Solution:
	def countAndSay(self, n: int) -> str:
		if n == 1:
			return '1'

		prev = self.countAndSay(n-1)

		result = ''
		flag = 1
		for i in range(len(prev) - 1):
			current = prev[i]
			next = prev[i+1]

			if current == next:
				flag += 1
			else:
				result += str(flag) + str(current)
				flag = 1
		result += str(flag) + str(prev[len(prev) - 1])

		return result
