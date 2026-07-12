class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
\
class Solution(object):
    def reverseBetween(self, head, left, right):
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        curr = prev.next

        for _ in range(right - left):
            temp = curr.next          # node to move
            curr.next = temp.next     # skip over it
            temp.next = prev.next     # point it to the current front of 
            prev.next = temp          # new front of the reversed section

        return dummy.next