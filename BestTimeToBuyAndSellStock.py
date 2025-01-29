class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheap=inf
        diff=0
        for i in range(len(prices)):
            cheap=prices[i] if prices[i]<cheap else cheap
            diff = max(diff,prices[i]-cheap)
        return diff