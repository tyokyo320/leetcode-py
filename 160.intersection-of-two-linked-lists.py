#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 遍历链表，计算链表长度
    def getListLength(self, head: ListNode):
        length = 0
        while head:
            length = length + 1
            head = head.next
        return length

    # 将指针向前移动至多出节点个数后面得位置
    def forwardLongList(self, long_len, short_len, head: ListNode):
        delta = long_len - short_len
        while head and delta:
            delta -= 1
            head = head.next
        return head

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        list_A_len = self.getListLength(headA)
        list_B_len = self.getListLength(headB)
        # 如果A链表长，移动headA到对应位置
        if list_A_len > list_B_len:
            headA = self.forwardLongList(list_A_len, list_B_len, headA)
        # 如果B链表长，移动headB到对应位置
        else:
            headB = self.forwardLongList(list_B_len, list_A_len, headB)
        
        while headA and headB:
            # 当两指针指向了同一个节点时，说明找到了
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None

# @lc code=end

