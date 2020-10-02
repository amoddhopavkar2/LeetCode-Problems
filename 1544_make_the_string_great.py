# 1544. Make the String Great

class Solution:
	def makeGood(self, s: str) -> str:
		flag = 1
		while flag:
			flag = 0
			temp = s
			for i in range(len(s)-1):
				if ord(s[i]) + 32 == ord(s[i+1]) or ord(s[i+1]) + 32 == ord(s[i]):
					temp = s[:i] + s[i+2:]
					flag = 1
					break
			s = temp
		return s
