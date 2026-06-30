class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr.sort()
        arr[-1] = -1
        return arr