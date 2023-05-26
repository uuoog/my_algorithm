# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        answer = 0
        def recursion(node, depth):
            nonlocal answer
            if node is None:
                return
            cur_depth = depth + 1
            answer = max(answer, cur_depth)
            recursion(node.left, cur_depth)
            recursion(node.right, cur_depth)

        recursion(root, 0)
        return answer
