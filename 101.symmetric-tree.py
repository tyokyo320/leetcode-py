#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    '''
    方法1：DFS(递归)，分解为树1左子树和树2的右子树是否为镜像，为树1右子树和树2的左子树是否为镜像
    时间复杂度：O(n)
    空间复杂度：O(n)

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.dfs(root, root)

    def dfs(self, node1, node2):
        # 树同时为空
        if not node1 and not node2:
            return True
        # 一边为空另一边非空
        if not node1 or not node2:
            return False

        # 两棵树都非空情况下，要求1：两棵树本身根节点相同，要求2：子树互为镜像
        return (node1.val == node2.val) and self.dfs(node1.left, node2.right) and self.dfs(node1.right, node2.left)
    '''

    '''
    方法2：BFS(队列)
    时间复杂度：O(n)
    空间复杂度：O(n)
    '''

    def isSymmetric(self, root: TreeNode) -> bool:
        # 双向队列，初始先把两个根节点推入
        queue = collections.deque([(root, root)])

        while queue:
            # 同时出队两次，拿出两个带比较的镜像节点
            node1, node2 = queue.popleft()
            # 树同时为空，继续
            if not node1 and not node2:
                continue
            # 一边为空，另一边非空
            elif not node1 or not node2:
                return False
            # 要求1：镜像节点值相同
            elif node1.val != node2.val:
                return False

            # 分别连续推入镜像子节点，要求2：子树互为镜像
            queue.append((node1.left, node2.right))
            queue.append((node1.right, node2.left))
        return True


# @lc code=end
