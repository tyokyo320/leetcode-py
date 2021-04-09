#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        left = self.getDepth(root.left)
        right = self.getDepth(root.right)

        # 如果二叉树中任意结点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树
        if abs(left - right) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def getDepth(self, node):
        '''
        leetcode 104
        '''
        if not node:
            return 0

        left = self.getDepth(node.left)
        right = self.getDepth(node.right)

        return max(left, right) + 1
# @lc code=end
