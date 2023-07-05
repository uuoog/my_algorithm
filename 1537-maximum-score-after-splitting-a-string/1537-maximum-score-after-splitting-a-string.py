class Solution:
    def maxScore(self, s: str) -> int:
        answer = []
        c = [c for c in s]
        for i in range(1, len(c)):
            answer.append(c[:i].count("0") + c[i:].count("1"))
        return max(answer)