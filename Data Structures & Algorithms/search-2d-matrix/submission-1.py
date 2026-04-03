class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # writing a lower bound (index for ele <= target )

        def lowerBound(nums):
            low = 0
            high = len(nums) - 1

            def check(mid):
                if nums[mid] >= target :
                    return 1
                else:
                    return 0

            ans = -1
            
            while low <= high :
                mid = low + (high - low) // 2
                if check(mid):
                    ans = mid 
                    high = mid - 1
                else:
                    low = mid + 1
            
            return ans

        last_array = []

        for i in range(len(matrix)):
            last_array.append(matrix[i][-1])
        
        lb = lowerBound(last_array)

        # if matrix[lb][-1] == target :
        #     return True
        
        second_array = matrix[lb]

        ans = lowerBound(second_array)

        if matrix[lb][ans] == target :
            return True
        return False