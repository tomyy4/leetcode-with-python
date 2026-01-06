from typing import List

nums = [2,7,11,15]
target = 9

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        i = 0
        n = len(nums)

        while i < n:
            op = target - nums[i]
            if op in seen:
                return [seen[op], i]
            else:        
                seen[nums[i]] = i
            i +=1

        return -1

s = Solution()
print(s.twoSum(nums=nums, target=target))
print(s.twoSum(nums = [3,2,4], target = 6))
print(s.twoSum(nums = [3,3], target = 6))
