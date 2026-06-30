class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()
        k=0
        for i in range(len(nums)):
            if nums[i] == val:
                nums.pop(i)
        k=len(nums)
        return k