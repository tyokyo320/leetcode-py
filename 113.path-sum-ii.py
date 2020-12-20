#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        result = []

        # 创建一个栈
        path = []
        path_value = 0
        self.preorder(root, sum, path_value, path, result)

        return result

    def preorder(self, node, sums, path_value, path, result):
        if not node:
            return

        path_value += node.val
        path.append(node.val)
        # print(path)

        # path_value等于sum且是叶节点
        if (path_value == sums) and (node.left is None) and (node.right is None):
            # 类比90题列表的引用，不能写成result.append(path)
            result.append(list(path))
            # print(result)
        
        self.preorder(node.left, sums, path_value, path, result)
        self.preorder(node.right, sums, path_value, path, result)

        path_value -= node.val
        path.pop()

# @lc code=end

