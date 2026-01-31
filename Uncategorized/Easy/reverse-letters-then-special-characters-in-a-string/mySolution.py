class Solution:
    def reverseByType(self, s: str) -> str:
        s1=[]
        s2=[]
        s=list(s)
        n=len(s)
        for ch in s:
            if ord(ch)<=122 and ord(ch)>=97:
                s1.append(ch)
            else:
                s2.append(ch)
        i,j=0,len(s1)-1
        while(i<j):
            s1[i],s1[j]=s1[j],s1[i]
            i+=1
            j-=1
        i,j=0,len(s2)-1
        while(i<j):
            s2[i],s2[j]=s2[j],s2[i]
            i+=1
            j-=1
        i,j=0,0
        for k in range(0,n):
            if ord(s[k])<=122 and ord(s[k])>=97:
                s[k]=s1[i]
                i+=1
            else:
                s[k]=s2[j]
                j+=1
        return "".join(s)