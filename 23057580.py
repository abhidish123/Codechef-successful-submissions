from collections import defaultdict as dd
for i in range(int(input())):
    S=list(str(input()))
    v=dd(int)
    for i in range(len(S)):
        v[S[i]]+=1
    l=list(v.values())
    l.sort(reverse=True)
    #print(l)
    z=sum(l)
    req1=len(S)-len(set(S))#if all become different
    req2=len(S)-max(l)#if all become same
    if(len(S)<=26):
        m1=min(req1,req2)
    else:
        m1=req2
    #print(m1)
    for i in range(2,int(z/2)+1):
        k=0
        c=0
        if(z%i==0 and int(z/i)<=26):
            n=int(z/i)
            k=1
            if(n>len(l)):
                c+=(n-len(l))*i
                for j in range(len(l)):
                    if(i-l[j]>0):
                        c+=(i-l[j])
            else:
                for j in range(n):
                    if(i-l[j]>0):
                        c+=(i-l[j])
        if(c<m1 and k==1):
            m1=c
        #print(m1)
    print(m1)
    