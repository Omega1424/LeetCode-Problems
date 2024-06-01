class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        maxx=0
        num_0 = 0

        for r in range(len(nums)):
            if nums[r]==0:
                num_0+=1
            while num_0>k:
                if nums[l]==0:
                    num_0-=1
                l+=1
            maxx = max(maxx,r-l+1)
        return maxx