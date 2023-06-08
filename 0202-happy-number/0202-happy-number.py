class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        answer = False
        while True:
            squared_sum = sum([int(x)**2 for x in str(n)])
            n = squared_sum
            if squared_sum == 1:
                answer = True
                break
            if squared_sum in visited:
                break
            visited.add(squared_sum)
        return answer
