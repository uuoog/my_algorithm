# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        from collections import deque

        q = deque([root])
        answer = []

        if not root:
            return answer
        
        while q:
            level_s = 0
            cnt = 0
            for _ in range(len(q)):
                cur = q.popleft()
                if cur is not None:
                    level_s += cur.val
                    cnt +=1
                    q.append(cur.left)
                    q.append(cur.right)
            if cnt:
                answer.append(level_s/cnt)
        return answer
