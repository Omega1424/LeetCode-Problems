class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr=prices[0]
        diff=0
        res=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                diff=prices[i]-prices[i-1]
                
            else:
                curr=prices[i]
                diff=0
            res+=diff if diff>0 else 0 
        return res