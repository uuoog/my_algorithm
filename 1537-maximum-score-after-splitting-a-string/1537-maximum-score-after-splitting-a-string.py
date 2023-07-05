class Solution:
    def maxScore(self, s: str) -> int:
        answer = []
        l_score = 0
        r_score = 0
        c = [c for c in s]
        for i in range(1, len(c)):
            c[:i].count("0")
            c[i:].count("1")
            answer.append(c[:i].count("0") + c[i:].count("1"))
        return max(answer)