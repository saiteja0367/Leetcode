class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead=set(deadends)
        if '0000' in deadends:
            return -1
        q=deque()
        q.append(['0000',0])
        visited = set(['0000'])
        while q:
            lock,turns=q.popleft()
            if lock==target:
                return turns
            for i in range(4):
                digit=int(lock[i])
                for move in (-1,1):
                    new_digit=(digit+move)%10
                    new_lock=lock[:i]+str(new_digit)+lock[i+1:]
                    if new_lock not in visited and new_lock not in dead:
                        visited.add((new_lock))
                        q.append((new_lock,turns+1))
        return -1


        