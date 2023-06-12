class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum= 0
        for num in nums:
            sum = sum + num
        return (n*(n+1)) // 2 - sum

