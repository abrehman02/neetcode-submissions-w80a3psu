class Solution:
    def rob(self, nums: List[int]) -> int:

        # what will dp store --> the maximum money we can get from the current i


        dp = [-1] * len(nums)

        def rec(i):
            if i >= len(nums) :
                return 0

            if dp[i] != -1 :
                return dp[i]

            ans = max(nums[i]+rec(i+2),rec(i+1))

            dp[i] = ans
            return ans
        
        rec(0)
        return dp[0]

            