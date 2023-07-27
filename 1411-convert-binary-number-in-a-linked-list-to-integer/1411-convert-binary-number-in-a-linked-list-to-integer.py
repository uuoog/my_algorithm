# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        cur = head
        answer = 0
        l = []
        while cur:
            l.append(cur.val)
            cur = cur.next
        l= l[::-1]
        for i in range(len(l)):
            answer += 2**i * l[i]
            print(l[i], answer)
        return answer