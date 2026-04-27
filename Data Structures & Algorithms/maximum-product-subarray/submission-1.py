class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = float('-inf')
        for i in range(len(nums)):
            product = nums[i]
            maxProd = nums[i]
            for j in range(i+1,len(nums)):
                product *= nums[j]
                maxProd = max(maxProd , product)
            ans = max(ans, maxProd)
        return ans