class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # derive this into the as discussed framwework and check function 

        def check(mid):
            if nums[mid] >= target :
                return True
            return False

        
        low = 0 
        high = len(nums) - 1

        ans = -1

        while low <= high :
            mid = low + (high - low) // 2
            if check(mid) :
                ans = mid 
                high = mid - 1
            else:
                low = mid + 1
        
        if nums[ans] == target :
            return ans
        return -1

    