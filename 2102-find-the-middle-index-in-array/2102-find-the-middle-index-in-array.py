class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        l_sum, r_sum = [], []
        l_prev, r_prev = 0, 0
        for i in range(len(nums)):
            l_sum.append(l_prev)
            l_prev += nums[i]
            r_sum = [r_prev] + r_sum
            r_prev += nums[len(nums) - 1 - i]
        answer = -1
        for i in range(len(l_sum)):
            if l_sum[i] == r_sum[i]:
                answer = i
                break
        return answer

