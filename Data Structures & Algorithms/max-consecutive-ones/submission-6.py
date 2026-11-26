class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_num = curr = 0
        for num in nums:
            if num == 1: 
                curr += 1
                max_num = max(max_num,curr)
            else:
                curr = 0
        return max_num