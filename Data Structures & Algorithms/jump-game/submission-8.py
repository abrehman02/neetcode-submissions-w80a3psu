class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [-1]*len(nums)
        def rec(i):
            if i >= len(nums) - 1 :
                return True
            if nums[i] == 0 :
                return False

            if dp[i] != -1 :
                return dp[i]

            for t in range(nums[i],0,-1):
                if i+t >= len(nums) - 1 :
                    return True
                ans = rec(i+t)
                dp[i] = ans
                if ans == True  :
                    return True
            return False
        
        return rec(0)