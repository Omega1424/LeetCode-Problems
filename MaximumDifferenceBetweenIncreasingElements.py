class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        #loop through
        maxdiff=-1
        minn=1e9
        for i in range(len(nums)):
            if nums[i]<=minn:
                minn=nums[i]
                continue
            else:
                maxdiff = max(maxdiff,nums[i]-minn)
        return maxdiff