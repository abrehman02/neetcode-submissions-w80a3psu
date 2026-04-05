class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        k = len(nums1) // 2 - 1
        if len(nums1) % 2 == 0 :
            return (nums1[k] + nums1[k+1])/2
        else:
            return nums1[k+1]