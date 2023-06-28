class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        c = Counter()
        for word in words:
            c += Counter(word)
        for v in c.values():
            if v % len(words) != 0:
                return False
                break
        return True

        
        