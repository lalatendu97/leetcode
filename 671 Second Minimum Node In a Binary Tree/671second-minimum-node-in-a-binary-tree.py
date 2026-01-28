# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        sm = []

        def call(node):
            sm.append(node.val)
            if node.left:
                call(node.left)
            if node.right:
                call(node.right)
            return
        
        call(root)
        sm = sorted(list(set(sm)))

        if len(sm) < 2:
            return -1
        return sm[1]

