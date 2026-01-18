

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1

        for i in range(n):
            if i not in nums:
                return i
        
s = Solution()
print(s.missingNumber(nums = [0,1]))
print(s.missingNumber(nums = [9,6,4,2,3,5,7,0,1]))