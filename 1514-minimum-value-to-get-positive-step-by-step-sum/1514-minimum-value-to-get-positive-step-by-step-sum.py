class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        startvalues = [x for x in range(1, len(nums)+1)]
        cum_sum = []
        prev = 0
        for num in nums:
            prev +=num
            cum_sum.append(prev)
        if min(cum_sum) <= 0:
            return abs(min(cum_sum)) + 1
        else:
            return 1
