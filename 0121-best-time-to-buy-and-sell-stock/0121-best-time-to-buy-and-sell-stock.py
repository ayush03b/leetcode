class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx = 0
        L = 0
        for R in range(1, len(prices)):
            if prices[R] < prices[L]:
                L=R
            else:
                maxx = max(maxx, prices[R] - prices[L])
        return maxx