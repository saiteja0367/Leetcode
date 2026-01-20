class Solution:
    def decodeString(self, s: str) -> str:
        s1=[] #for numbers
        s2=[] #for strings
        num=0
        res=''
        for char in s:
            if char.isdigit():
                num=num*10+int(char)
            elif char=='[':
                s1.append(num)
                s2.append(res)
                num=0
                res=''
            elif char==']':
                repeat=s1.pop()
                prev_str=s2.pop()
                res=prev_str+repeat*res
            else:
                res+=char
        return res
            


        
        
        