# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        answer = 0

        if not root:
            return answer

        from collections import deque
        q = deque([(root, root.val)])

        while q:
            cur_node, max_ = q.popleft()
            if cur_node.val >= max_:
                answer += 1
                max_ = cur_node.val
            if cur_node.left:
                q.append((cur_node.left, max_))
            if cur_node.right:
                q.append((cur_node.right, max_))
        return answer