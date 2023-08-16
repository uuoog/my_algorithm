class Solution:
    def climbStairs(self, n: int) -> int:
        # if n <= 1:
        #     return 1
        # dp = [0] * (n+1)
        # dp[0] = dp[1] = 1

        # for i in range(2, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[n]

        dp = [0, 1, 2]
        if n <=2:
            return dp[n]
        
        for i in range(3, n+1):
            dp.append(dp[i-1] + dp[i-2])
        return dp[-1]