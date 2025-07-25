class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        L, R = 0, len(height) - 1

        while L <= R:
            area = min(height[L], height[R]) * (R-L)
            ans = max(ans, area)
            if height[L] <= height[R]:
                L+=1
            else:
                R-=1

        return ans