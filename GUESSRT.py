from sys import stdin
from fractions import Fraction

mod=1000000007
def fast_power(base,power):
    result=1
    while power>0:
        if power%2==1:
            result=(result*base)%mod
        power=power//2
        base=(base*base)%mod
    return result
for _ in range(int(stdin.readline())):
    n,k,m=map(int,stdin.readline().split())
    g=(m//2)+1
    if m%2==0:
        q=fast_power(n,g-1)*(n+k)
        p=q-(fast_power(n-1,g-1)*(n+k-1))
    else:
        q=fast_power(n,g)
        p=q-fast_power(n-1,g)
    q=fast_power(q,mod-2)%mod
    print((p*q)%mod)
