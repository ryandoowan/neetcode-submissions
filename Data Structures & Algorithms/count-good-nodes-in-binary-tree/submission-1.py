# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = [root.val]

        def func(node: TreeNode, ans: List, num: int):
            if node == None:
                return
            if node.val >= num:
                ans.append(node.val)
                num = node.val
            
            func(node.left, ans, num)
            func(node.right, ans, num)

        func(root.left, ans, root.val)
        func(root.right, ans, root.val)
        return len(ans)