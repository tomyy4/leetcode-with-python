from typing import List


"""
Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
"""

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        n = len(arr)

        for i in range(n):
            double = arr[i] * 2

            if double in seen:
                return True
            

            if arr[i] % 2 == 0 and arr[i] // 2 in seen:
                return True
            
            seen.add(arr[i])
        
        return False

s = Solution()
print(s.checkIfExist(arr=[10,2,5,3])) # true
print(s.checkIfExist(arr=[3,1,7,11])) # false
print(s.checkIfExist(arr=[30,24, 15, 50])) # true
print(s.checkIfExist(arr=[7,1,14,11])) # true
print(s.checkIfExist(arr=[0,-2,2])) # false
print(s.checkIfExist(arr=[0,0])) # True