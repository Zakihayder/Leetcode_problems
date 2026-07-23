class Solution(object):
    def connect(self, root):
        if not root:
            return None

        curr = root

        while curr:
            head = None      # First node of next level
            prev = None      # Previous node in next level

            while curr:

                if curr.left:
                    if prev:
                        prev.next = curr.left
                    else:
                        head = curr.left
                    prev = curr.left

                if curr.right:
                    if prev:
                        prev.next = curr.right
                    else:
                        head = curr.right
                    prev = curr.right

                curr = curr.next

            curr = head

        return root