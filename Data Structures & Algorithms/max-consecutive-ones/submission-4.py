class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_cons_ones = 0
        current = 0
        for num in nums:
            if (num==1):
                current += 1
            else:
                if max_cons_ones < current:
                    max_cons_ones = current
                current = 0

        if max_cons_ones < current:
                max_cons_ones = current
        return max_cons_ones
