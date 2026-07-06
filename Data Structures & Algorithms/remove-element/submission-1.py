class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()
        kk=0
        for i in range(len(nums)):
            if nums[i] == val:
                nums.pop(i)
        kk=len(nums)
        return kk
