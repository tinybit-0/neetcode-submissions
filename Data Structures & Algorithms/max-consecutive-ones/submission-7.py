class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        lenn = 0
        maxxx = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                lenn+=1
            else:
                continue
            maxxx = lenn
        return maxxx
            
