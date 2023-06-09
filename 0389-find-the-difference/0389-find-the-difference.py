class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        from collections import Counter
        text_s = [x for x in str(s)]
        text_t = [x for x in str(t)]
        counter_s = Counter(text_s)
        counter_t = Counter(text_t)
        for key in counter_t:
            if counter_s[key] < counter_t[key]:
                return key
