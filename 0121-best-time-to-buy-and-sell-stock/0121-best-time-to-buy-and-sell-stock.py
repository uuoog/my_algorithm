class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        cur_min = prices[0]
        for i in range(1, len(prices)):
            profit = prices[i] - cur_min
            if profit > answer:
                answer = profit
            if cur_min > prices[i]:
                cur_min = prices[i]
        return answer