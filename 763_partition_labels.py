# 763 - Partition Labels

class Solution:
	def partitionLabels(self, S: str) -> List[int]:
		result = []
		last_index = [0] * 26

		for i in range(len(S)):
			last_index[ord(S[i]) - ord('a')] = i

		start, end = 0, 0
		for i in range(len(S)):
			end = max(end, last_index[ord(S[i]) - ord('a')])

			if end == i:
				result.append(end - start + 1)
				start = end + 1
		return result
