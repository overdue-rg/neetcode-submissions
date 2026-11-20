class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        curr = 0
        for num in nums:
            if num == 1:
                curr += 1
            else:
                curr = 0
            if curr > max_count:
                    max_count = curr
        return max_count