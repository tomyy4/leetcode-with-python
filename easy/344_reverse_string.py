

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        head = 0
        tail = len(s) - 1

        while head < tail:
            s[head], s[tail] = s[tail], s[head]
            head += 1
            tail -= 1

s1 = ["h", "e", "l", "l", "o"]
s2 = ["H", "a", "n", "n", "a", "h"]
s3 = ["A", "b", "b", "a"]

s = Solution()

s.reverse_string(s1)
s.reverse_string(s2)
s.reverse_string(s3)