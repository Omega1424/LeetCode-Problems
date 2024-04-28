class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res=nums[0]+nums[1]+nums[2]
        nums=sorted(nums)
        for i in range(len(nums)-2):
            j=i+1
            k=len(nums)-1
            while j<k:
                sum=nums[i]+nums[j]+nums[k]
                if sum==target:
                    return sum
                if abs(sum-target)<abs(res-target):
                    res = sum
                if sum<target:
                    j+=1
                else:
                    k-=1
        return res
        