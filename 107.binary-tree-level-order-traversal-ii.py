#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        result, queue = [], [root]

        while any(queue):
            length = len(queue)
            temp = []
            for _ in range(length):
                p = queue.pop(0)
                temp.append(p.val)

                if p.left:
                    queue.append(p.left)
                if p.right:
                    queue.append(p.right)
            result.append(temp)
        
        result.reverse()
        return result
# @lc code=end

