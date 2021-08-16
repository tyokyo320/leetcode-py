#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#

# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        item = []
        self.sumPath(root, item)
        return self.sum

    def sumPath(self, root: Optional[TreeNode], item: List[int]):
        if not root:
            return

        item.append(root.val)

        # 当这个位置是叶子节点的时候，求和
        if not root.left and not root.right:
            self.sum += int(''.join([str(x) for x in item]))
            print('叶子节点：', root.val, self.sum)
        else:
            # left
            self.sumPath(root.left, item)
            # right
            self.sumPath(root.right, item)

        item.pop()

# @lc code=end
