#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        '''
        递归

        if not root:
            return False
        if not root.left and not root.right and root.val == targetSum:
            return True
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
        '''

        '''
        DFS
        '''
        # Directly call the helper method.
        return self.dfs(root, 0, targetSum)

    def dfs(self, root, currSum, targetSum):
        # Return if the root is None.
        if not root:
            return False

        # Add the current root's value to currSum.
        currSum += root.val

        # If both the child nodes are None and currSum is equal to TargetSum,
        # we have found the right path.
        if root.left == None and root.right == None and currSum == targetSum:
            return True

        # Check if the right path can be found on the left subtree or the right subtree.
        return self.dfs(root.left, currSum, targetSum) or self.dfs(root.right, currSum, targetSum)


# @lc code=end
