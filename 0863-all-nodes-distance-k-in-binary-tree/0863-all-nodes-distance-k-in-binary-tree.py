# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        from collections import deque
        parent = {}
        def build_parent(node, par):
            if not node:
                return
            parent[node] = par
            build_parent(node.left, node)
            build_parent(node.right, node)

        # build parent mapping
        build_parent(root, None)

        # BFS from target
        q = deque([target])
        visited = set([target])
        distance = 0

        while q:
            size = len(q)

            if distance == k:
                return [node.val for node in q]

            for _ in range(size):
                node = q.popleft()

                # move to left child
                if node.left and node.left not in visited:
                    visited.add(node.left)
                    q.append(node.left)

                # move to right child
                if node.right and node.right not in visited:
                    visited.add(node.right)
                    q.append(node.right)

                # move to parent
                par = parent[node]
                if par and par not in visited:
                    visited.add(par)
                    q.append(par)

            distance += 1
        return []

