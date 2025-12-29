# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # def bfs(root):
        #     if not root:
        #         return []
        #     result=[]
        #     queue=[root]
        #     while queue:
        #         len_size=len(queue)
        #         for i in range(len_size):
        #             node=queue.pop(0)
        #             if i==0:
        #                 result.append(node.val)
        #             if node.right:
        #                 queue.append(node.right)
        #             if node.left:
        #                 queue.append(node.left)
        #     return result
        # return bfs(root)
        result = []
        def dfs(node, level):
            if not node:
                return
            if level == len(result):
                result.append(node.val)
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
        dfs(root, 0)
        return result


        