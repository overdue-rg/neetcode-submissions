class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            max_val = 0
            for j in range(i+1, len(arr)):
                if max_val < arr[j] or max_val == arr[j]:
                    max_val = arr[j]
                    arr[i] = arr[j]
        arr[-1] = -1
        return arr