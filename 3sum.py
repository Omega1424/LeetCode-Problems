def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res=[]
        temp=[]
        if len(nums) < 3:
            return res
        for i in range(len(nums)):
            if nums[i]>0:
                break
            if i>=1:
                if nums[i]==nums[i-1]:
                    continue
            l,r = i+1,len(nums)-1
            while l<r:
                if nums[i]+nums[l]+nums[r]==0:
                    temp.append(nums[i])
                    temp.append(nums[l])
                    temp.append(nums[r])
                    res.append(temp)
                    temp=[]
                    low=nums[l]
                    high=nums[r]
                    while l<r and nums[l]==low:
                        l+=1
                    while l<r and nums[r]==high:
                        r-=1
                elif nums[i]+nums[l]+nums[r]>0:
                    r-=1
                    
                else:
                    l+=1
        return res