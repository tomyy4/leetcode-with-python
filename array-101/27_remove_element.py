from typing import List

a = [3,2,2,3]
val = 3
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fast = 0
        slow = 0

        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow +=1
            fast +=1
        
        return slow

s = Solution()
print(s.removeElement(a, val))