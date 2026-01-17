"""
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        i = 0
        j = 0
        output = ""
        while i < len(s):
            if s[i] == " ":
                tmp = s[j:i]
                output += tmp[::-1] + " "
                j = i + 1
            i +=1

        remaining = s[j:i]
        return output + remaining[::-1]
    
s = Solution()
print(s.reverseWords("Let's take LeetCode contest"))
print(s.reverseWords("Mr Ding"))