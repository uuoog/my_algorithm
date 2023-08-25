class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        ans = 0
        while nums:
            l = str(nums.pop(0))
            r = ""
            if nums:
                r = str(nums.pop())
            ans += int(l+r)
        return ans
