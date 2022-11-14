class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        res=False
        for i in range(len(nums)):
            if i==0:
                continue
            else:
                if nums[i]==nums[i-1]:
                    res = True
        return res
                    