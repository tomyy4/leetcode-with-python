from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # we could use a sort algorithm
        return sorted([n*n for n in nums])


s = Solution()
print(s.sortedSquares(nums=[-4,-1,0,3,10]))
print(s.sortedSquares(nums=[-7,-3,2,3,11]))