#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
        path = []
        node_p_path = []
        node_q_path = []
        finish = 0
        
        self.preorder(root, p, path, node_p_path, finish)
        # print(node_p_path[0])
        
        # 清空path，finish，计算q节点路径
        path.clear()
        finish = 0
        self.preorder(root, q, path, node_q_path, finish)

        #print(node_q_path[0])
        lp = node_p_path[0]
        lq = node_q_path[0]

        if len(lp) < len(lq):
            path_len = len(lp)
        else:
            path_len = len(lq)
        # print(path_len)

        result = TreeNode(0)
        for i in range(path_len):
            if lp[i] == lq[i]:
                result = lp[i]

        return result

    
    def preorder(self, node, search, path, result, finish):
        # finish未找到为0，找到为1
        if (node is None) or finish:
            return
        
        path.append(node)
        if node == search:
            finish = 1
            result.append(list(path))
            result = result[0]
            # print(result)
        
        self.preorder(node.left, search, path, result, finish)
        self.preorder(node.right, search, path, result, finish)

        path.pop()



        
# @lc code=end

