#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        '''
        方法1：递归
        if head == None or head.next == None:
            return head
        
        head.next.next, head.next, head = head, self.swapPairs(head.next.next), head.next
        return head
        '''

        '''
        方法2：
        '''
        temp = head
        while head and head.next:
            # 交换
            head.val, head.next.val = head.next.val, head.val
            # 移动到下一组第一个
            head = head.next.next
            
        return temp

# @lc code=end

