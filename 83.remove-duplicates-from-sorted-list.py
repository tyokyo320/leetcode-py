#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        temp = head
        while temp and temp.next:
            if temp.val == temp.next.val:
                # skip duplicated node
                temp.next = temp.next.next
            else:
                # not duplicate of current node, move to next node
                temp = temp.next
        return head





# @lc code=end

