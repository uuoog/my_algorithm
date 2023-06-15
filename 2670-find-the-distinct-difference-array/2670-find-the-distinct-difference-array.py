class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            result = (len(set(nums[0:i+1]))) - (len(set(nums[i+1:])))
            answer.append(result)
        return answer
