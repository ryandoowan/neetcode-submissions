# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def func(self, node: TreeNode, ans: List, num: int):
        if node == None:
            return
        if node.val >= num:
            ans.append(node.val)
            num = node.val
        
        self.func(node.left, ans, num)
        self.func(node.right, ans, num)

    def goodNodes(self, root: TreeNode) -> int:
        ans = [root.val]

        self.func(root.left, ans, root.val)
        self.func(root.right, ans, root.val)
        return len(ans)