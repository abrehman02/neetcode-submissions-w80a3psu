class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = float('-inf')
        prefix = suffix = 0
        n = len(nums)
        for i in range(n):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[n - i - 1] * (suffix or 1)
            ans = max(prefix , suffix, ans)
        return ans