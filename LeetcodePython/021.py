# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        tmp = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next
        if l1 != None:
            tmp.next = l1
        else:
            tmp.next = l2
        return dummy.next


a = Solution()
l1, l1.next, l1.next.next, l1.next.next.next = ListNode(1), ListNode(6), ListNode(7), ListNode(9)
l2, l2.next, l2.next.next = ListNode(3), ListNode(5), ListNode(8)

print a.mergeTwoLists(l1, l2).next.next.next.val