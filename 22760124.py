'''Example Input
2
3
abcaa="abc"
bcbd="bcd"
bgc="bcg"
3
quick
brown
fox
Example Output
2
0'''
for i in range(int(input())):
    n=int(input())
    g=n
    v=""
    mn=201
    while(n):
        s=str(input())
        d1=set(s)
        if(len(d1)<mn):
            mn=len(d1)
            z="".join(d1)
            z=list(z)
            #print(z)
        d="".join(set(s))
        v=v+d
        n-=1
    l=list(v)
    #print(l)
    cn=0
    for i in range(mn):
        if(l.count(z[i])==g):
            #print(l[i])
            cn+=1
    print(cn)     