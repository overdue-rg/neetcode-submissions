class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max:int     = 0
        current:int = 0
        for num in nums:
            if num == 1:
                current += 1
            else:
                current = 0
            if current > max:
                max = current
        return max
            