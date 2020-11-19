#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution():
    def partition(self, head, x):
        new_list1 = []
        new_list2 = []
        while head is not None:
            # print(head.val)
            if head.val < x:
                new_list1.append(head.val)
            else:
                new_list2.append(head.val)
            head = head.next
        new_list1 = new_list1 + new_list2
        print(new_list1)

        new_node = ListNode()
        r_node = new_node
        for i in new_list1:
            temp = ListNode(i)
            r_node.next, temp.next = temp, None
            r_node = r_node.next

        return new_node.next


if __name__ == "__main__":
    n1 = ListNode(1, None)
    n2 = ListNode(4, None)
    n3 = ListNode(3, None)
    n4 = ListNode(2, None)
    n5 = ListNode(5, None)
    n6 = ListNode(2, None)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6

    s = Solution()
    s.partition(n1, 3)


# @lc code=end
