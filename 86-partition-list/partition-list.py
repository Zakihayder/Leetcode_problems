class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)
        less = less_dummy
        greater = greater_dummy

        curr = head
        while curr:
            if curr.val < x:
                less.next = curr
                less = less.next
            else:
                greater.next = curr
                greater = greater.next
            curr = curr.next

        greater.next = None          
        less.next = greater_dummy.next  # connect the two lists

        return less_dummy.next