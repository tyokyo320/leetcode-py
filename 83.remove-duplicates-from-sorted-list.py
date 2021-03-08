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
        '''
        方法1：
        每一次都比较当前节点和下一个节点的值，如果不同，就将当前节点后移，
        如果相同，就不改变当前节点，直至下一个节点的值与当前节点的值不相等
        temp = head
        while temp and temp.next:
            if temp.val == temp.next.val:
                # skip duplicated node
                temp.next = temp.next.next
            else:
                # not duplicate of current node, move to next node
                temp = temp.next
        return head
        '''

        '''
        方法2：递归
        首先递归要确定递归结束的条件, 所以 if 条件就给出了递归结束的情况
        head.next = deleteDuplicates(head.next) 这句代码保证了 从 head.next 到链表的结尾, 都没有重复的结点
        要决定的是 head 指向当前的 head 还是 head.next, 通过比较值可以得到. 如果值不相同, 就从 head 开始, 加上后面不重复的链表
        如果值相同, 就直接指向后面不重复的链表即可
        '''
        if head == None or head.next == None:
            return head
        # 要决定的是 head 指向当前的 head 还是 head.next
        head.next = self.deleteDuplicates(head.next)
        return head.next if head.val == head.next.val else head

# @lc code=end