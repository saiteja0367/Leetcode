class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:

        #we will be assigning new groups to -1 items
        new_group_id=m
        for i in range(n):
            if group[i]==-1:
                group[i]=new_group_id
                new_group_id+=1
        total_groups=new_group_id

        #we will build the graphs for items and groups
        item_graph=defaultdict(list)
        item_indegree=[0]*n
        group_graph=defaultdict(list)
        group_indegree=[0]*total_groups
        for curr in range(n):
            for prev in beforeItems[curr]:
                #itemgraph
                item_graph[prev].append(curr)
                item_indegree[curr] += 1
                #groupgraph (only if differnt groups)
                if group[prev]!=group[curr]:
                    group_graph[group[prev]].append(group[curr])
                    group_indegree[group[curr]]+=1
        #we will write the topological sort function
        def topo_sort(graph,indegree,nodes):
            queue=deque()
            result=[]
            for node in nodes:
                if indegree[node]==0:
                    queue.append(node)
            while queue:
                node=queue.popleft()
                result.append(node)
                for nei in graph[node]:
                    indegree[nei]-=1
                    if indegree[nei]==0:
                        queue.append(nei)
            if len(result)==len(nodes):
                return result
            return []
        #we will toposort the groups
        group_order = topo_sort(group_graph, group_indegree, list(range(total_groups)))
        if not group_order:
            return []
        #we will toposort the items
        item_order = topo_sort(item_graph, item_indegree, list(range(n)))
        if not item_order:
            return []
        #we will arrange the items by group
        group_to_items = defaultdict(list)
        for item in item_order:
            group_to_items[group[item]].append(item)
        #we will build the final result following the group order
        result = []
        for grp in group_order:
            result.extend(group_to_items[grp])
        return result


        #t.c->o(n+dependencies)
        #s.c->o(n+dependencies)
        


        