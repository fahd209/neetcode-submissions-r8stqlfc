# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = deque([(root, 0)])
        tree_level = []

        if root == None:
            return []

        while queue:

            node, level = queue.popleft()

            if level > len(tree_level) - 1:
                tree_level.append([node.val])
            else:
                tree_level[level].append(node.val)

            if node.left:
                queue.append((node.left, level + 1))

            if node.right:
                queue.append((node.right, level + 1))

            


        return tree_level