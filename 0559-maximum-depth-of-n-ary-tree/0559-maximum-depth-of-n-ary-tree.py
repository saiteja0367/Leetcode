"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def helper(node):
            if not node:
                return 0
            max_depth=0
            for child in node.children:
                max_depth=max(max_depth,helper(child))
            return 1+max_depth
        return helper(root)
        