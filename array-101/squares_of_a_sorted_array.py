from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # we could use a sort algorithm
        return sorted([n*n for n in nums])


### REFACTOR DAY 3 ######
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ordered = [n for n in nums]
        left,right = 0, len(nums) -1
        pos = len(nums)- 1
        while left <= right:
            if abs(nums[right]) > abs(nums[left]):
                ordered[pos] = nums[right] * nums[right]
                right -=1
            else:
                ordered[pos] = nums[left] * nums[left]
                left +=1
            pos -=1

        return ordered

nums_1=[-4,-1,0,3,10]
nums_2=[-7,-3,2,3,11]
s = Solution()
print(s.sortedSquares(nums=nums_1))
print(s.sortedSquares(nums=nums_2))