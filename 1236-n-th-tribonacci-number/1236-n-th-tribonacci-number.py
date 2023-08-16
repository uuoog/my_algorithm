class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]
        if n == 0:
            return dp[n]
        
        for i in range(0, n-2):
            x = dp[i] + dp[i+1] + dp[i+2]
            dp.append(x)
        return dp[-1]