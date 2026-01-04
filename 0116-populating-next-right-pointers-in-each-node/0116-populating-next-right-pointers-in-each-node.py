"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # if not root:
        #     return None
        # q=deque([root])
        # while q:
        #     size=len(q)
        #     prev=None
        #     for _ in range(size):
        #         node=q.popleft()
        #         if prev:
        #             prev.next=node
        #         prev=node
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     prev.next=None
        # return root

        #s.c-0(n)
        #t.c -0(n)

        if not root:
            return None
        leftmost=root
        while leftmost.left:
            curr=leftmost
            while curr:
                curr.left.next=curr.right
                if curr.next:
                    curr.right.next=curr.next.left
                curr=curr.next
            leftmost=leftmost.left
        return root





        