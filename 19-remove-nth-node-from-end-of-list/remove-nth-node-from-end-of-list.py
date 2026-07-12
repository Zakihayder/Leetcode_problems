def getLength(head):
    length = 0
    curr = head
    while curr:
        length+=1
        curr = curr.next
    return length

class Solution(object):
    def removeNthFromEnd(self, head, n):

        length = getLength(head)

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(length-n):
            prev = prev.next

        prev.next = prev.next.next

        for _ in range(n-1):
            prev = prev.next
        
        return dummy.next


            
        