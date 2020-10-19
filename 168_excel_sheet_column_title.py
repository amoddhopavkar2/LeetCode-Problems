# 168 - Excel Sheet Column Title

class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ''
        while n > 0:
            n -= 1
            res += chr(65 + (n % 26))
            n = n // 26
        return res[::-1]
