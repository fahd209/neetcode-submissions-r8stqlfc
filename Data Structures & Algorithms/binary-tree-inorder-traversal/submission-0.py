# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        in_order = []
        
        if root == None:
            return []

        def dfs(cur):

            if cur == None:
                return

            dfs(cur.left)
            in_order.append(cur.val)
            dfs(cur.right)

        dfs(root)


        return in_order