# 1588 - Sum of All Odd Length Subarrays

class Solution:
	def sumOddLengthSubarrays(self, arr: List[int]) -> int:
		result = 0
		for i in range(len(arr)):
			count, sum = 0, 0
			for j in range(i, len(arr)):
				sum += arr[j]
				count += 1

				if count % 2 == 1:
					result += sum
		return result
