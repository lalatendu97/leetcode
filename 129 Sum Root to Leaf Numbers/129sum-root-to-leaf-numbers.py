# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []
        def call(root, s=""):
            if root.left == None and root.right == None:
                res.append(s + str(root.val))
                return

            if root.left != None:
                call(root.left, s + str(root.val))

            if root.right != None:
                call(root.right, s + str(root.val))
            return

        call(root)
        sum = 0
        for i in res:
            sum += int(i)
        return sum