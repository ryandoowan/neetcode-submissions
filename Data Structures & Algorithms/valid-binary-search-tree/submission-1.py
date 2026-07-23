# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def func(node: TreeNode, low: int, high: int):
            if (node == None):
                return True
            elif (low < node.val < high):
                return func(node.left, low, node.val) and func(node.right, node.val, high)
            else:
                return False

        return func(root.left, -math.inf, root.val) and func(root.right, root.val, math.inf)
        