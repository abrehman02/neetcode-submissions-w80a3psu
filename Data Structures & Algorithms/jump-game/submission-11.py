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
                if rec(i+t):
                    dp[i] = True
                    return True
            dp[i] = False
            return False
        
        return rec(0)
        # goal = len(nums) - 1

        # for i in range(len(nums)-2,-1,-1):
        #     if i + nums[i] >= goal :
        #         goal = i
        
        # if goal <= 0 :
        #     return True
        # return False