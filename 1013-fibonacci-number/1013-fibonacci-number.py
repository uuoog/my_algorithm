class Solution:
    def fib(self, n: int) -> int:
        dp = [0, 1]
        if n <= 0:
            return dp[n]
        
        for i in range(n - 1):
            dp.append(dp[i] + dp[i+1])
        return dp[-1]