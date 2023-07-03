class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        answer = -1
        for i in range(len(words)):
            l = words[(startIndex - i) % n]
            r = words[(startIndex + i) % n]
            if target in [l, r]:
                answer = i
                break
        return answer
