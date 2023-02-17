'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Results:
    Runtime: 50 ms
    Memory Usage: 17.1 MB
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def recursiveTree(root: Optional[TreeNode], result: list):
            if root is None:
                return result
            recursiveTree(root.left, result)
            result.append(root.val)
            recursiveTree(root.right, result)
            
        result = []
        recursiveTree(root, result)
        
        base = result[0]
        for i in result[1:]:
            if i > base:
                base = i
            else:
                return False
        return True
        
        
        
        
