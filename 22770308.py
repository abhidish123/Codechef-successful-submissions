'''
Example Input
2
4
1 1 4 1
3 4 2 1
7
5 4 5 4 5 4 5
3 2 4 7 2 5 9
Example Output
3
-1
'''
for i in range(int(input())):
    n=int(input())
    at=[int(x) for x in input().split()]
    df=[int(x) for x in input().split()]
    v=[]
    for i in range(n):
        atc=0
        j=i
        if(i-1<0):
            atc+=at[i+1]
            i=i+n-1
            atc+=at[i]
            if(df[j]>atc):
                v.append(df[j])
        elif(i+1>n-1):
            atc+=at[i-1]
            i=i-n+1
            atc+=at[i]
            if(df[j]>atc):
                v.append(df[j])
        else:
            atc+=at[i+1]+at[i-1]
            if(df[j]>atc):
                v.append(df[j])
    if(len(v)==0):
        print(-1)
    else:
        print(max(v))