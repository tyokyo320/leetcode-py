#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        '''
        方法1：deque 双向队列
        '''
        if not root:
            return []  # base case
        res = []
        # queue to colloct all the nodes
        queue = deque([root])

        while queue:
            level_vals = []  # hold the values at the current level.
            for _ in range(len(queue)):  # evalute once before execution enter the loop
                node = queue.popleft()
                level_vals.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level_vals)
        return res

        '''
        方法2：利用list当作队列实现

        result, queue = [], [root]

        # 这里不可以写成while q:，因为当输入是[]，这个时候q=[[]]
        while any(queue):
            temp = []
            length = len(queue)
            for _ in range(length):
                # 队头节点出队
                p = queue.pop(0)
                temp.append(p.val)
                if p.left:
                    queue.append(p.left)
                if p.right:
                    queue.append(p.right)
            result.append(temp)
                
        return result
        '''
# @lc code=end
