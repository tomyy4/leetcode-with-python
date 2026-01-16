class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq_s = {}
        freq_t = {}

        for c in s:
            if c in freq_s:
                freq_s[c] += 1
            else:
                freq_s[c] = 1

        for j in t:
            if j in freq_t:
                freq_t[j] += 1
            else:
                freq_t[j] = 1

        for i,v in freq_t.items(): 
            if i in freq_s and v != freq_s[i]:
                return i
            
            if i not in freq_s:
                return i
        

s = Solution()
print(s.findTheDifference(s = "abcd", t = "abcde"))
print(s.findTheDifference(s = "a", t = "aa"))
print(s.findTheDifference(s= "", t = "y"))