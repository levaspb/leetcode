'''
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

COMMENT: need to be improved
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def recursiveCompare(l_tree: Optional[TreeNode], r_tree: Optional[TreeNode]):
            if l_tree.val != r_tree.val:
                return False
            if l_tree.left == r_tree.left == l_tree.right == r_tree.right == None:
                return True
            
            if l_tree.left != None and r_tree.right == None:
                return False
            if l_tree.left == None and r_tree.right != None:
                return False
            if l_tree.right != None and r_tree.left == None:
                return False
            if l_tree.right == None and r_tree.left != None:
                return False
                
            if l_tree.left == None and r_tree.right == None:
                return recursiveCompare(l_tree.right, r_tree.left)
            elif l_tree.right == None and r_tree.left == None:
                return recursiveCompare(l_tree.left, r_tree.right)
            else:
                if recursiveCompare(l_tree.left, r_tree.right):
                    return recursiveCompare(l_tree.right, r_tree.left)
                else:
                    return False
                
        if root.left == None and root.right == None:
            return True
        if root.left == None and root.right != None:
            return False
        if root.right == None and root.left != None:
            return False
        return recursiveCompare(root.left, root.right)
