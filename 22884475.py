'''
Example Input
1
6 2 3 3
Example Output
Win
'''
def gcd(a,b):
    if(b==0):
        return a 
    return gcd(b,a%b)

for i in range(int(input())):
    n,a,b,k=[int(x) for x in input().split()]
    #print(k)
    f=gcd(a,b)
    lc=(a*b)/f
    p1=n//a
    p2=n//b
    p3=n//lc
    k1=int(p1+p2-2*p3)
    if(k1>=k):
        print("Win")
    else:
        print("Lose")