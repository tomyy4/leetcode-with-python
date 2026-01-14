class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = {}

        for i in range(len(s)):
            if s[i] not in seen:
                seen[s[i]] = 1
            else:
                seen[s[i]] += 1

                if seen[s[i]] == 2:
                    return s[i]


s = Solution()
print(s.repeatedCharacter(s="abccbaacz")) # c
print(s.repeatedCharacter(s="abcdd")) # d
print(s.repeatedCharacter(s="aabbc")) # a
print(s.repeatedCharacter(s="abcbabc")) # a