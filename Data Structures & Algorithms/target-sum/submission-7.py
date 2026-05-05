class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # the range of value can be from -sum(nums) --> +sum(nums)
        dp = {}

        def rec(i,value):
            
            # base
            if i == len(nums):
                if value == target:
                    return 1
                else :
                    return 0
            
            # caching 
            # if (i , value) in dp :
                # return dp[(i, value)]
            # transition
            ans = rec(i+1 , value - nums[i]) + rec(i+1 , value + nums[i])
            # dp[(i , value)] = ans
            # saveAndReturn
            return ans
            
        return rec(0,0)