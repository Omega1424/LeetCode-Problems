class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l,r=0,0
        maxx=0

        while r<len(nums):
            if nums[r]==0:
                r+=1
                l=r
            else:
                maxx=max(maxx,r-l+1)
                r+=1
        return maxx

        