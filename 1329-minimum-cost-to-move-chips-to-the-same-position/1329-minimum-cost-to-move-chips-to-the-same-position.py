class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        cost = 0
        even_cnt = []
        odd_cnt = []
        for i in range(len(position)):
            if position[i] % 2 == 0:
                even_cnt.append(position[i])
            if position[i] % 2 == 1:
                odd_cnt.append(position[i])
        print(even_cnt, odd_cnt)
        cost = min(len(even_cnt), len(odd_cnt))
        return cost



           