class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while True:
            for i in range(0,32):
                if n == 2 ** i:
                    return True
            return False
