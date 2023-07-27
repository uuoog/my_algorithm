# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 순회 2 번???
        cur = head
        cnt = 0
        while cur:
            cnt += 1
            cur = cur.next
            mid = cnt//2
        cur = head
        for i in range(mid):
            cur = cur.next
        return cur