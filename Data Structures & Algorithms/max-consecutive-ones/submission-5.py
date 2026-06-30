class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        lenn = 0
        maxx = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                lenn+=1
            maxx = lenn
            lenn = 0
        return maxx
            