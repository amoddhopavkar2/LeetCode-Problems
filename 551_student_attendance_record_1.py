# 551 - Student Attendance Record - I

from collections import Counter
class Solution:
	def checkRecord(self, s: str) -> bool:
		cnt = Counter(s)

		if cnt['A'] > 1:
			return False
		
		for i in range(1, len(s) - 1, 1):
			if s[i - 1] == 'L' and s[i] == 'L' and s[i + 1] == 'L':
				return False

		return True
		
