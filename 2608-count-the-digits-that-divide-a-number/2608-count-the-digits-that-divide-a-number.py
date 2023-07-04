class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        num_str = [x for x in str(num)]
        for i in range(len(num_str)):
            if num % int(num_str[i]) == 0:
                count += 1
        return count
