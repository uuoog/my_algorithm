class Solution:
    def getLucky(self, s: str, k: int) -> int:
        l = "".join([str(ord(c) - 96) for c in s])
        for i in range(k):
            l = sum([int(c) for c in str(l)])
        return l
