'''
Example Input
2   
4   
1 1 1 1   
2   
1 4   
Example Output
1   
4
'''
for i in range(int(input())):
    n=int(input())
    l=[int(x) for x in input().split()]
    z=[x-1 for x in l]
    print(sum(z)+1)