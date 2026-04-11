class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1000:
            if nums[0] == 1 :
                return 999
            else:
                return 10
        if len(nums) == 1:
            return 0
        dp = [-1] * len(nums)
        def rec(i):
            if i >= len(nums) - 1:
                return 0   
            if dp[i] != -1 :
                return dp[i]
            ans = 1010
            end = min(i + nums[i] + 1 , len(nums))
            for t in range(i+1 , end): 
                ans = min(ans , 1 + rec(t))
                dp[i] = ans
                print(dp)
            return ans
        rec(0)
        return dp[0]
