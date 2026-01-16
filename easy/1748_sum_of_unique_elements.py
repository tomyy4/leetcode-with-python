from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq = {}
        result = 0

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        for i, v in freq.items():
            if v == 1:
                result += i

        return result
    
s = Solution()
print(s.sumOfUnique(nums=[1,2,3,2,1])) # 6
print(s.sumOfUnique(nums=[1,2,3,2])) # 4
print(s.sumOfUnique(nums=[1,1,1])) # 1
print(s.sumOfUnique(nums=[10,20,30,10])) # 60