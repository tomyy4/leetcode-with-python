
from typing import List

"""
Refactor
"""
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        seq = []
        arr_len = len(arr)
        for num in arr:
            seq.append(num)
            if len(seq) == arr_len:
                break
            
            if num == 0:
                seq.append(0)
            
            if len(seq) == arr_len:
                break
            
        for i, v in enumerate(seq):
            arr[i] = v


s = Solution()
s.duplicateZeros(arr=[1,0,2,3,0,4,5,0])
s.duplicateZeros(arr=[0,0,0,0,0,0,0])
s.duplicateZeros(arr=[1,5,2,0,6,8,0,6,0])