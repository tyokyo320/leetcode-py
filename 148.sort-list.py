#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        '''
        分割
        '''
        # 递归停止条件
        if not head or not head.next:
            return head
        
        # p用来记录slow前面位置
        p, slow, fast = None, head, head
        while fast and fast.next:
            p = slow
            slow = slow.next
            fast = fast.next.next
        # 分割成2个部分
        p.next = None

        return self.mergeTwoLists(self.sortList(head), self.sortList(slow))

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        leetcode 21
        '''
        dummy = ListNode(None)
        current = dummy

        # 将current与较小的节点进行连接
        while l1 and l2:
            if l1.val < l2.val:
                current.next, l1 = l1, l1.next
            else:
                current.next, l2 = l2, l2.next
            # current指向新连接的节点
            current = current.next
        
        # 若l1有剩余，将l1接到current后
        if l1:
            current.next = l1
        elif l2:
            current.next = l2

        return dummy.next


# @lc code=end

