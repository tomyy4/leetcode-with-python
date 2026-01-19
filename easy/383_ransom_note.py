class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_freq = {}
        magazine_freq = {}

        for n in ransomNote:
            if n in note_freq:
                note_freq[n] += 1
            else:
                note_freq[n] = 1
        
        for i in magazine:
            if i in magazine_freq:
                magazine_freq[i] += 1
            else:
                magazine_freq[i] = 1
        
        for i,v in note_freq.items():
            if i not in magazine_freq:
                return False
            
            if i in magazine_freq and v > magazine_freq[i]:
                return False
        
        return True

s = Solution()
print(s.canConstruct(ransomNote = "a", magazine = "b"))
print(s.canConstruct(ransomNote = "aa", magazine = "ab"))
print(s.canConstruct(ransomNote = "aa", magazine = "aab"))
print(s.canConstruct(ransomNote = "bg", magazine =
"efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"))