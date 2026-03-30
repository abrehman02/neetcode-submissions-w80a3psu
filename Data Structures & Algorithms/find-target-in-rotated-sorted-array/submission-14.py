class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def check(mid, low, high):
            if nums[low] <= nums[mid]:
                return nums[low] <= target < nums[mid]
            else:
                return not nums[mid] < target <= nums[high]

        # the framework

        low = 0
        high = len(nums) - 1
        ans = -1

        while low <= high :
            mid = low + (high - low) // 2
            if nums[mid] == target :
                ans = mid 
            
            if check(mid , low , high):
                high = mid - 1
            else:
                low = mid + 1
        
        return ans


