# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        lst1 = []
        lst2 = []
        
        def calll(node):
            if not node:
                return
            lst1.append(node.val)
            if node.left:
                calll(node.left)
            else:
                lst1.append(None)
            if node.right:
                calll(node.right)
            else:
                lst1.append(None)
            return

        def callr(node):
            if not node:
                return
            lst2.append(node.val)
            if node.left:
                callr(node.left)
            else:
                lst2.append(None)
            if node.right:
                callr(node.right)
            else:
                lst2.append(None)
            return

        calll(p)
        callr(q)
        
        return lst1 == lst2
        