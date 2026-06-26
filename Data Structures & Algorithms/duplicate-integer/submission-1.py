class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        alreadyy = []
        for i in nums:
            if i not in alreadyy:
                alreadyy.append(i)
            else:
                return True
        return False