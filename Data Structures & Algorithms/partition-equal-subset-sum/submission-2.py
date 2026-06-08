class Solution:
    def canPartition(self, nums: List[int]) -> bool:
       # since we need to divide the array into two parts 
       # the target is half (sum) // 2
        target = sum(nums) // 2
        if sum(nums) % 2 : 
            return False
        dp = [[-1] * (target+1) for _ in range(len(nums)+1)]
        def rec(i , target):
            if i >= len(nums):
                return False
            if i == len(nums) - 1 and target == 0 :
                return True
            if dp[i][target] != -1:
                return dp[i][target]
            ans = rec(i+1 , target - nums[i]) or rec(i+1 , target)
            dp[i][target] = ans
            return ans

        return rec(0 , target)

       