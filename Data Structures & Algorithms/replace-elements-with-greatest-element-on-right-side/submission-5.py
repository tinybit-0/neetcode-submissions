class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i=0
        while i<len(arr)+1:
            if arr[i]<arr[i+1]:
                arr[i] = arr[i+1]
            i+=1
        return arr