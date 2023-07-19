class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        answer = 0
        index = []
        for i in range(1,len(nums)+1):
            if len(nums) % i == 0:
                index.append(i)
        for i in index:
            answer += nums[i-1]*nums[i-1]
        return answer
            

