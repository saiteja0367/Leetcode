"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:


        #t.c->o(n)
        #s.c->o(h) #recursion stack
        # res=[]
        # def helper(root):
        #     if not root:
        #         return None
        #     for child in root.children:
        #         helper(child)
        #     res.append(root.val)
        # helper(root)
        # return res


        #iterative
        if not root:
            return []
        stack=[root]
        res=[]
        while stack:
            node=stack.pop()
            res.append(node.val)
            for children in node.children:
                stack.append(children)
        return res[::-1]
        