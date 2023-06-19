class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        if set(nums1).intersection(set(nums2)):
            result = min(list(set(nums1).intersection(set(nums2))))
            return result
        else:
            f = (min(nums1) * 10) + min(nums2)
            s =(min(nums2) * 10) + min(nums1)
            if f > s:
                return s
            else:
                return f