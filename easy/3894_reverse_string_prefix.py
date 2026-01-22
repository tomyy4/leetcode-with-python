

class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        a = s[0:k][::-1]
        b = s[k:]
        return a + b

s = Solution()
print(s.reversePrefix("abcd", 2))
print(s.reversePrefix(s="xyz", k = 3))