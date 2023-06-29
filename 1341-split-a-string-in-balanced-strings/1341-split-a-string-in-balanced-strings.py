class Solution:
    def balancedStringSplit(self, s: str) -> int:
        c_s = [c for c in s]
        L_count = 0
        R_count = 0
        total_count = 0
        for i in range(len(c_s)):
            if c_s[i] == "L":
                L_count += 1
            if c_s[i] == "R":
                R_count += 1
            if L_count == R_count:
                total_count += 1
        return total_count

            
