class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        first = -1
        prev_critical = -1
        min_dist = float('inf')

        prev = head
        curr = head.next
        index = 1

        while curr and curr.next:
            nxt = curr.next

            if ((prev.val < curr.val and curr.val > nxt.val) or
                (prev.val > curr.val and curr.val < nxt.val)):

                if first == -1:
                    first = index
                else:
                    min_dist = min(min_dist, index - prev_critical)

                prev_critical = index

            prev = curr
            curr = nxt
            index += 1

        if first == -1 or first == prev_critical:
            return [-1, -1]

        max_dist = prev_critical - first

        return [min_dist, max_dist]