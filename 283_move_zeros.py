
from typing import List

arr = [0,1,0,3,12]
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        fast = 0
        n = len(nums)

        while fast < n:
            if nums[fast] != 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]
                slow +=1
            fast +=1

s = Solution()
s.moveZeroes(nums=arr)