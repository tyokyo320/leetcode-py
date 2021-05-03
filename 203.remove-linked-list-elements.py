#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        '''
        方法1
        while head is not None and head.val == val:
            head = head.next
        current = head

        while current is not None:
            # 看后面还有没有
            if current.next is not None and current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        
        return head
        '''

        '''
        方法2：
        '''
        current, prev = head, None
        
        while current:
            if current.val == val:
                # 删除该节点
                if current == head:
                    current = head = head.next
                else:
                    prev.next = current.next
                    current = current.next
            else:
                # 寻找下一个
                prev = current
                current = current.next
        
        return head


# @lc code=end

