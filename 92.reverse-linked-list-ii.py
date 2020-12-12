#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # 计算需要逆置的节点个数
        change_len = n - m + 1
        pre_head = None
        result = head

        # head向前移动m-1个位置，记录该节点前驱和该节点
        while head and m - 1:
            pre_head = head
            head = head.next
            m = m - 1
        
        modify_list_tail = head
        new_head = None

        # 从head开始，逆置change_len = n-m+1ge节点
        while head and change_len:
            temp = head.next
            head.next = new_head
            new_head = head
            head = temp
            change_len = change_len - 1

        # 将pre_head与new_head连接，modify_list_tail与head链接
        modify_list_tail.next = head

        if pre_head:
            pre_head.next = new_head
        else:
            # 如果pre_head为空，说明m=1从第一个节点开始逆置，结果即为逆置后的头节点
            result = new_head

        return result

# @lc code=end

