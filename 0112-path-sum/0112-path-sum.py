# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        from collections import deque

        answer = False
        if not root:
            return answer

        q = deque([(root, 0)])

        while q:
            cur, cur_sum = q.popleft()
            cur_sum += cur.val
            if not cur.left and not cur.right:
                if cur_sum == targetSum:
                    answer = True
            if cur.left:
                q.append((cur.left, cur_sum))
            if cur.right:
                q.append((cur.right, cur_sum))
        return answer
