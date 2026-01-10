class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        path=[]
        def dfs(start):
            if start==len(s):
                res.append(path[:])
                return 
            for end in range(start,len(s)):
                sub_string=s[start:end+1]
                if sub_string==sub_string[::-1]:
                    path.append(sub_string)
                    dfs(end+1)
                    path.pop()
        dfs(0)
        return res


