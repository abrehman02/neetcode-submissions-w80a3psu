class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n+1)
        def rec(i):
            if i == 1 or i == 2:
                return i
            if dp[i] != -1 :
                return dp[i]
            ans = rec(i-1) + rec(i-2)
            dp[i] = ans
            return ans
        return rec(n)