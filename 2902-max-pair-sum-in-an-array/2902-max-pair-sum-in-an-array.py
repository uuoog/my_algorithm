class Solution:
    def maxSum(self, nums: List[int]) -> int:
        ans = -1

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                num_a = nums[i]
                num_b = nums[j]
                num_a_arr = [int(c) for c in str(num_a)]
                num_b_arr = [int(c) for c in str(num_b)]

                # if max(num_a_arr) == max(num_b_arr):
                #     ans = max(ans, num_a + num_b)
                if max(num_a_arr) != max(num_b_arr):
                    continue
                ans = max(ans , num_a + num_b)

        return ans
