# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        answer = 0
        if not root:
            return answer

        q = deque([(root, False)])
        
        while q:
            cur, is_left = q.popleft()
            if not cur.left and not cur.right and is_left == True:
                answer += cur.val
            if cur.left:
                q.append((cur.left, True))
            if cur.right:
                q.append((cur.right, False))
        return answer