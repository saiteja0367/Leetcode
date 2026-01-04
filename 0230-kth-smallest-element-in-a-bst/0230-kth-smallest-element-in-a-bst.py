# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count=0
        curr=root
        while curr:
            if not curr.left:
                count+=1
                if count==k:
                    return curr.val
                curr=curr.right
            else:
                pred=curr.left
                while pred.right and pred.right!=curr:
                    pred=pred.right
                if not pred.right:
                    pred.right=curr
                    curr=curr.left
                else:
                    pred.right=None
                    count+=1
                    if count==k:
                        return curr.val
                    curr=curr.right
            