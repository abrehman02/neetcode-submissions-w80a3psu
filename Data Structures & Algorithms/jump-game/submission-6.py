class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        def rec(i):
            if i >= len(nums) - 1 :
                return True
            
            if nums[i] == 0 :
                return False

            for t in range(nums[i],0,-1):
                if i+t >= len(nums) - 1 :
                    return True
                ans = rec(i+t)
                if ans == True:
                    return ans
            
            return False
        
        return rec(0)