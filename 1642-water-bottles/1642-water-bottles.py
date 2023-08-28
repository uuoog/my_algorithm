class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        e_bottle = 0
        ans = 0
        while numBottles > 0:
            ans += numBottles
            e_bottle += numBottles
            numBottles = e_bottle // numExchange
            e_bottle = e_bottle % numExchange
            print(numBottles, e_bottle)
        return ans
