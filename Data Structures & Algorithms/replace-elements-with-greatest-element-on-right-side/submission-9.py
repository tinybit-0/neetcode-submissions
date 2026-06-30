class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i=1
        for i in range (len(arr)):
            if arr[i-1]<arr[i]:
                arr[i] = arr[i+1]
            i+=1
        arr[-1] = -1
        return arr