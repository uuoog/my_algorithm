# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        from collections import deque

        q = deque([(root, [])])
        answer = 1

        while q:
            cur_node, path = q.popleft()
            if path and cur_node.val >= max(path):
                answer += 1

            if cur_node.left:
                q.append((cur_node.left, path +[cur_node.val]))
            if cur_node.right:
                q.append((cur_node.right, path +[cur_node.val]))
        return answer