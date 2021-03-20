#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        '''
        方法1：递归dfs
        只需要判断当前节点是否为空，不为空则返回它的下一层节点的高度加一，否则返回0
        
        递归的结束条件: 当节点为叶子节点的时候.
        递归的子问题: 当前最大深度 = 左右子树最大深度的较大者 + 1
        '''
        if not root:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        
        


        
# @lc code=end

