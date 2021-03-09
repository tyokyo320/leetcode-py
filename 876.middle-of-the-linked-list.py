#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        '''
        对比leetcode 148
        '''
        if not head and not head.next:
            return head
        
        p, slow, fast = None, head, head
        while fast and fast.next:
            p = slow
            slow = slow.next
            fast = fast.next.next
        
        return slow

        
# @lc code=end

