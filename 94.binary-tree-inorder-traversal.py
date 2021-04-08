#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.traverse_path = []

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            self.inorderTraversal(root.left)
            self.traverse_path.append(root.val)
            self.inorderTraversal(root.right)

            return self.traverse_path

# @lc code=end
