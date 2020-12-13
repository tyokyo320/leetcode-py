#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 快慢指针
        fast = head
        slow = head
        # 相遇的节点
        meet = None

        while fast:
            slow = slow.next
            fast = fast.next

            # 如果fast遇到链表尾，则返回none            
            if not fast:
                return None
            
            # fast再走一步
            fast = fast.next
            
            if fast == slow:
                # return True
                # fast与slow相遇，记录相遇位置
                meet = fast
                break
        # return False
        
        if meet == None:
            # 如果没有相遇，则说明无环
            return None
        
        while head and meet:
            # 当head与meet相遇，说明遇到环得起始位置
            if head == meet:
                return head
            head = head.next
            meet = meet.next
        return None
  
# @lc code=end

