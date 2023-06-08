class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        d = defaultdict(list)
        answer = []

        for word in strs:
            print(word, "".join(sorted([x for x in word])))
            d["".join(sorted([x for x in word]))].append(word)
        return list(d.values())
