class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while prev.next and prev.next.next:
            if prev.next.val == prev.next.next.val:
                # found a duplicate run — remember the value, skip all nodes with it
                dup_val = prev.next.val
                while prev.next and prev.next.val == dup_val:
                    prev.next = prev.next.next
                # do NOT advance prev here — prev.next is now a fresh node to check
            else:
                prev = prev.next

        return dummy.next