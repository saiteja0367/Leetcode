class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        graph={}
        for i in range(len(friends)):
            graph[i]=friends[i]
        visited=set()
        queue=deque()
        def bfs(i):
            current_level=0
            queue.append(i)
            visited.add(i)
            while queue:
                if current_level==level:
                    break
                for _ in range(len(queue)):
                    node=queue.popleft()
                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            queue.append(neighbor)
                            visited.add(neighbor)
                current_level+=1
            freq=Counter()
            for person in queue:
                for video in watchedVideos[person]:
                    freq[video]+=1
            result = sorted(freq.keys(), key=lambda x: (freq[x], x))
            return result
        return bfs(id)

        