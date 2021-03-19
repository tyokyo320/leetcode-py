#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    '''
    方法1：dfs递归
    '''

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.dfs(p, q)

    def dfs(self, node1, node2):

        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        return (node1.val == node2.val) and self.dfs(node1.left, node2.left) and self.dfs(node1.right, node2.right)
# @lc code=end
