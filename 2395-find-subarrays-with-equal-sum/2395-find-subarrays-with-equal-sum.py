class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        set_value = set()
        for i in range(len(nums)-1):
            s = nums[i] + nums[i+1]
            if s in set_value:
                return True
            set_value.add(s)
        return False
