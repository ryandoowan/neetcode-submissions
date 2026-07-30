# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        ans = [[root.val]]
        def func(node, ans, index):
            if node == None:
                return
            if len(ans) < index + 1:
                ans.append([])
            ans[index].append(node.val)

            func(node.left, ans, index + 1)
            func(node.right, ans, index + 1)

        func(root.left, ans, 1)
        func(root.right, ans, 1)

        return ans