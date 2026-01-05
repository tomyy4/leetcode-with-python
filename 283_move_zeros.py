
arr = [0,1,0,3,12]

"""
##### first iteration #####
- No swaps
- resulting array = [0,1,0,3,12]
- slow=0, fast=1

##### second iteration #####
- resulting array = [1,0,0,3,12]
- slow=1, fast=2

##### third iteration #####
- resulting array = [1,0,0,3,12]
slow=1, fast=3

##### fourth iteration #####
resulting array = [1,3,0,0,12]
slow=2, fast=4

##### fifth iteration #####
resulting array = [1,3,12,0,0]
slow=3, fast=5

"""
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