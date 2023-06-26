class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        from collections import Counter
        c1 = Counter(word1)
        c2 = Counter(word2)
        diff = ((c1 - c2) + (c2 - c1))
        answer = True
        print(diff)
        for k in diff:
            print(k, diff[k])
            if diff[k] > 3:
                return False
        return answer 
