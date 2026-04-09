class Solution:
    def rob(self, nums: List[int]) -> int:        
        if len(nums) == 1:
            return nums[0]
        dp = [[-1] * 2 for _ in range(len(nums))]
        def rec(i , start ):
            if i == len(nums) - 1 and start == 0:
                return 0
            if i >= len(nums):
                return 0
            if dp[i][start] != -1 :
                return dp[i][start]
            
            ans = max(nums[i] + rec(i+2,start),rec(i+1,start))
            dp[i][start] = ans
            return ans

        return max(rec(0,0) , rec(1,1))
        # ----> transition
        # i + money, i+2 
        # also for last tc store first 