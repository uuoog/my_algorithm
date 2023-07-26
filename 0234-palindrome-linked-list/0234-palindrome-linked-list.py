# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur = head
        l = []
        answer = False
        while cur:
            l.append(cur.val)
            cur = cur.next
        w = ''.join(str(x) for x in l)
        if w == w[::-1]:
            answer =True
        return answer