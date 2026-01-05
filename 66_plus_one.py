from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for digit in digits:
            num += str(digit)
        
        op = str(int(num) + 1)
        return [int(num) for num in op]


s = Solution()
print(s.plusOne_2([1,2,3]))
print(s.plusOne_2([9]))