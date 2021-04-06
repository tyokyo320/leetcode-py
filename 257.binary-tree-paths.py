#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []

        self.result = []
        self.dfs(root, str(root.val))
        return self.result

    def dfs(self, node, path):
        if not node.left and not node.right:
            self.result.append(path)
        if node.left:
            self.dfs(node.left, path + "->" + str(node.left.val))
        if node.right:
            self.dfs(node.right, path + "->" + str(node.right.val))


# @lc code=end
