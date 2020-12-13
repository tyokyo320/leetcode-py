#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp_head = ListNode(None)
        pre = temp_head

        # 将pre与较小的节点进行连接
        while l1 and l2:
            if l1.val < l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            # pre指向新连接的节点
            pre = pre.next
        
        # 如果l1有剩余，将l1接到pre后
        if l1:
            pre.next = l1
        if l2:
            pre.next = l2
        return temp_head.next
 
# @lc code=end

