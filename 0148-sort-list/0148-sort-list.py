class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case
        if not head or not head.next:
            return head

        # Step 1: Split using slow-fast pointers
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Cut the list into two halves
        prev.next = None

        # Step 2: Sort both halves
        left = self.sortList(head)
        right = self.sortList(slow)

        # Step 3: Merge
        return self.merge(left, right)

    def merge(self, l1,l2):
        dummy = ListNode(0)
        curr = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next   # 🔴 IMPORTANT

        # Attach remaining nodes
        curr.next = l1 if l1 else l2
        return dummy.next
