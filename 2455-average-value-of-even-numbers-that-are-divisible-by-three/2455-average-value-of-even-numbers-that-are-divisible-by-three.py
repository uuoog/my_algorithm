class Solution:
    def averageValue(self, nums: List[int]) -> int:
        l = []
        for num in nums:
            if (num % 6 == 0):
                l.append(num)
        if len(l) > 0:
            return sum(l) // len(l)
        else:
            return 0
