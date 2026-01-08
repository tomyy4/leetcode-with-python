from typing import List

#Input: nums = [0,0,1,1,1,2,2,3,3,4]
#Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        fast = 1
        slow = 1

        while fast < len(nums):
            # if it's different from the previous value, we've found a unique value
            if nums[fast] != nums[fast -1]:
                nums[slow] = nums[fast]
                slow += 1
            fast +=1
        
        return slow

s = Solution()
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))