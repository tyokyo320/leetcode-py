#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        new_head = None
        while head:
            # 第一步首先需要备份，备份后才可以修改head指针
            tmp = head.next
            head.next = new_head
            new_head = head
            head = tmp
            
        return new_head


if __name__ == "__main__":
    n1 = ListNode(1, None)
    n2 = ListNode(2, None)
    n3 = ListNode(3, None)
    n4 = ListNode(4, None)
    n5 = ListNode(5, None)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = None

    s = Solution()
    s.reverseList(n1)

# @lc code=end

