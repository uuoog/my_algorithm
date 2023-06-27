class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        l_cum_sum = []
        r_cum_sum = []
        l_prev = 0
        r_prev = 0
        for i in range(len(nums)):
            l_cum_sum.append(l_prev)
            l_prev += nums[i]
            r_cum_sum = [r_prev] + r_cum_sum
            r_prev += nums[len(nums)- 1- i]
        print(l_cum_sum)
        print(r_cum_sum)
        for i in range(len(nums)):
            if l_cum_sum[i] == r_cum_sum[i]:
                return i
        return -1
