#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        '''
        方法1：BFS
        '''
        if not root:
            return 0
        
        queue = deque([(1, root)])
        while len(queue) != 0:
            depth, p = queue.popleft()

            if not any((p.right, p.left)):
                return depth
            else:
                depth += 1
                if p.left != None:
                    queue.append((depth, p.left))
                if p.right != None:
                    queue.append((depth, p.right))
# @lc code=end

