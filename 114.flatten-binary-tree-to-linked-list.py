#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        node_list = []
        self.preorder(root, node_list)

        for i in range(1, len(node_list)):
            node_list[i-1].left = None
            node_list[i-1].right = node_list[i]
    
    def preorder(self, node, node_list):
        if node is None:
            return
        
        node_list.append(node)
        self.preorder(node.left, node_list)
        self.preorder(node.right, node_list)
        
# @lc code=end

