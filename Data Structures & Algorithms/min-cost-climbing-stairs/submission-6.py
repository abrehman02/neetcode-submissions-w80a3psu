class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # transitions --> i+1 , i __ min
        # base case --> if i >= n :
        # return 0 because we are storing the cost in the way
        # think of the transitions state first for a brute force solution
        # dp will store the min cost to reach the end 

        dp = [-1] * len(cost)
        def rec(i):
            if i >= len(cost):
                return 0 
            if dp[i] != -1:
                return dp[i]
            ans = cost[i]
            ans += min(rec(i+1) , rec(i+2)) 
            dp[i] = ans
            return ans
        return min(rec(0),rec(1))