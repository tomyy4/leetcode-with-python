
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word

        fast = 0
        while fast < len(word):
            if word[fast] == ch:
                break
            fast +=1
        
        str_to_reverse = word[0:fast+1]
        return str_to_reverse[::-1] + word[fast+1:]

s = Solution()
print(s.reversePrefix(word="abcdefd", ch="d"))
print(s.reversePrefix(word="abcdef", ch="zs"))
print(s.reversePrefix(word="abcdef", ch="f"))
print(s.reversePrefix(word="ab", ch="b"))
print(s.reversePrefix(word="ab", ch="a"))
print(s.reversePrefix(word="aba", ch="b"))
print(s.reversePrefix(word="bbbbba", ch="a"))
