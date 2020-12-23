#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
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
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return 

        q = deque()
        q.append(root)
        return_list = []
        while len(q) > 0:
            ans = []
            
            for i in range(len(q)):
                node = q.popleft()
                
                ans.append(node.val)

                if node.left is not None:
                    q.append(node.left)

                if node.right is not None:
                    q.append(node.right)

            # store the last element of each level 
            return_list.append(ans[-1])
        
        return return_list

        
# @lc code=end

