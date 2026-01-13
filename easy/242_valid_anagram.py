class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        s_hash_table = {}
        t_hash_table = {}

        for i in range(len(s)):
            if s[i] in s_hash_table:
                s_hash_table[s[i]] += 1
            else:
                s_hash_table[s[i]] = 1
        
        for j in range(len(t)):
            if t[j] in t_hash_table:
                t_hash_table[t[j]] += 1
            else:
                t_hash_table[t[j]] = 1
        
        
        return s_hash_table == t_hash_table        

s = Solution()
print(s.isAnagram(s = "anagram", t = "nagaram"))