class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 1
        while nums[slow] != nums[fast] :
            slow += 1
            fast += 2
            slow = slow % len(nums)
            fast = fast % len(nums)
            if slow == fast:
                slow -= 1

        return nums[slow]