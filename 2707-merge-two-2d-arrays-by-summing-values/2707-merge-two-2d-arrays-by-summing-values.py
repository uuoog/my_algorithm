class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        c1 = Counter(dict(nums1))
        c2 = Counter(dict(nums2))
        d = c1 + c2
        answer = [[k, v] for k, v in sorted(d.items())]
        return answer
