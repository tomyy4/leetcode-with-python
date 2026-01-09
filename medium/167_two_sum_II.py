from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            result = numbers[left] + numbers[right]

            if result == target:
                return [left + 1, right + 1]
            elif result < target:
                left += 1
            else:
                right -= 1
        
        return -1
  

s = Solution()
print(s.twoSum(nums=[2,7,11,15], target=9))
print(s.twoSum(nums=[2,3,4], target=6))
print(s.twoSum(nums=[-1,0], target=-1))
print(s.twoSum(nums=[8,4], target=2))
print(s.twoSum(nums=[1, 2, 4, 7, 11], target=9))