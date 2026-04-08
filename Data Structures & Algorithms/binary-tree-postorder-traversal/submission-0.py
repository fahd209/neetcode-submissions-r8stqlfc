# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        post_order = []

        def dfs(cur):

            if cur == None:
                return

            dfs(cur.left)
            dfs(cur.right)
            post_order.append(cur.val)

        dfs(root)


        return post_order