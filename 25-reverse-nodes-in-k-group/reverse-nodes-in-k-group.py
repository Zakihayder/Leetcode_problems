

def getLength(head):
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        return length

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if not head:
            return head

        length = getLength(head)
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        left = 1
        right = k

        for _ in range(length/k):
            curr = prev.next

            for _ in range(k-1):
                temp = curr.next          # node to move
                curr.next = temp.next     # skip over it
                temp.next = prev.next     # point it to the current front of reversed section
                prev.next = temp          
            prev = curr

        return dummy.next