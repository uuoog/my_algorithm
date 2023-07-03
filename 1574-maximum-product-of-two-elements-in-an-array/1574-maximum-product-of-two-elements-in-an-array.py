class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        answer = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if ((nums[i] - 1) * (nums[j] -1) > answer) and (i != j):
                    answer = (nums[i] - 1) * (nums[j] -1)
        return answer