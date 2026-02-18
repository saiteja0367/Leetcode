# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        column_map = defaultdict(list)
        queue = deque([(root, 0, 0)])
        
        while queue:
            node, col, row = queue.popleft()
            column_map[col].append((row, node.val))
            if node.left:
                queue.append((node.left, col - 1, row + 1))
            if node.right:
                queue.append((node.right, col + 1, row + 1)) 
        result = []
        for col in sorted(column_map.keys()):
            column_map[col].sort()
            result.append([val for row, val in column_map[col]])
        
        return result