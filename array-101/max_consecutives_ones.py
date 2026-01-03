from typing import List

### FIRST ATTEMPT #####
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # will store the sequences
        seqs = []
        current_seq = 0
        for value in nums:
            if value == 1:
                current_seq += 1
            else:
                # we've found a 0, reset and push
                seqs.append(current_seq)
                current_seq = 0                

        # if current_seq is not 0, push it to the seqs list so we do not forget any sequence
        if current_seq != 0:
            seqs.append(current_seq)
        return max(seqs)




##### REFACTOR DAY 2 #####
def max_consecutives_ones(nums):
    max_count = 0
    current_seq = 0

    for num in nums:
        if num == 1:
            current_seq += 1
        else:
            if current_seq > max_count:
                max_count = current_seq
            current_seq = 0
    
    # in case the 1 sequence ends without a zero and it's greater than current max_count
    if current_seq > 0 and current_seq > max_count:
            max_count = current_seq
    
    return max_count

nums = [1,1,0,1,1,1]
nums2 = [1,0,1,1,0,1]
s = Solution()
print(s.findMaxConsecutiveOnes(nums=nums))
print(s.findMaxConsecutiveOnes(nums=nums2))
print(max_consecutives_ones(nums=nums))
print(max_consecutives_ones(nums=nums2))