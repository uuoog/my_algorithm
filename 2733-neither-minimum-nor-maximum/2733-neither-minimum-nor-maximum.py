class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) == 2 or len(nums) == 1:
            answer = -1
            return answer
        else:
            return nums[1]
