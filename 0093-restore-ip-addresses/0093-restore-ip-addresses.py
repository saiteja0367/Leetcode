class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n=len(s)
        res=[]
        def backtrack(index,path):
            if index==len(s) and len(path)==4:
                res.append('.'.join(path))
                return
            if len(path)==4:
                return
            for length in range(1,4):
                if index+length>len(s):
                    break
                segment=s[index:index+length]
            #we shouldn't have leading zeros
                if segment[0]=='0' and len(segment)>1:
                    break
                if int(segment)>255:
                    continue
                path.append(segment)
                backtrack(index+length,path)
                path.pop()
        backtrack(0,[])
        return res

        #t.c->roughly 0(1)
        #s.c->o(4) (recursiondepth+result storage)
                            
        