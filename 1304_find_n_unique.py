# 1304 - Find N Unique Integers Sum up to Zero

class Solution:
	def sumZero(self, n: int) -> List[int]:
		result = []

		if n % 2 == 0:
			for i in range(1, n//2 + 1):
				result.append(i * 3)
				result.append(-i * 3)

		else:
			for i in range(-n//2 + 1, n//2 + 1):
				result.append(i)

		return result