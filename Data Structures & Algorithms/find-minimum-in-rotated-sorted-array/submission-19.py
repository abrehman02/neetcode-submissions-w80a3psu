class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        def parse(mid):
            if nums[mid] < nums[0]:
                return 1
            else:
                return 0

        
        low = 0
        high = len(nums) - 1
        ans = 0
        while low <= high :
            mid = low + (high - low) // 2
            if parse(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return nums[ans]