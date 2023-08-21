class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        c = ""
        for i in range(len(words)):
            c += words[i][0]
        if s == c:
            return True
