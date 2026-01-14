"""
Input: s = "leetcode"
Output: 0
-----------
Input: s = "loveleetcode"
Output: 2
-----------
Input: s = "aabb"
Output: -1
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        i = 0
        length = len(s)
        while i < length:
            if s[i] in freq:
                freq[s[i]] +=1
            else:
                freq[s[i]] = 1

            i +=1
        
        j = 0

        while j < length:
            if s[j] in freq and freq[s[j]] == 1:
                return j
            j +=1
        
        return -1

s = Solution()
print(s.firstUniqChar(s="leetcode"))
print(s.firstUniqChar(s="loveleetcode"))