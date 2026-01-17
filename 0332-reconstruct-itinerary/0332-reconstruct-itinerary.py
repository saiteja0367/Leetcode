class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)

        # Step 1: sort tickets so we get lexicographically smallest destination
        tickets.sort(reverse=True)
        for src, dst in tickets:
            adj[src].append(dst)

        res = []

        def dfs(src):
            # Step 2: consume edges permanently
            while adj[src]:
                next_dst = adj[src].pop()
                dfs(next_dst)
            # Step 3: postorder add
            res.append(src)

        dfs("JFK")
        return res[::-1]
                



