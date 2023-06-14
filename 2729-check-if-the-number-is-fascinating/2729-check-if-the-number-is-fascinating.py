class Solution:
    def isFascinating(self, n: int) -> bool:
        n_two = n*2
        n_three = n*3
        n_concat = str(n)+str(n_two)+str(n_three)
        list_n = list(n_concat)
        int_list_n = [int(x) for x in list_n]
        if sorted(int_list_n) == list(range(1,10)):
            return True
        else:
            return False
