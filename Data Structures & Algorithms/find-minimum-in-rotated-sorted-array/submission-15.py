class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        def check(mid , low , high):    
            return nums[mid] <= nums[high]

        # the framework

        low = 0
        high = len(nums) - 1
        ans = 1001

        while low <= high :
            mid = low + (high - low) // 2
            if check(mid , low , high):
                ans = min(nums[mid] , ans)
                high = mid - 1
            else:
                low = mid + 1
        
        return ans


