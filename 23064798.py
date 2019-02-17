for i in range(int(input())):
    v=[]
    xl=0
    yl=0
    xu=100
    yu=100
    cj=1
    while(cj!=0):
        if(yl<=100):
            print(*('Q',xl,yl))
            #yl+=1
            x=int(input())
            if(x==0):
                cj=0
                v.append(xl)
                v.append(yl)
            yl+=1
        else:
            xl+=1
            yl=0
    dj=1
    while(dj!=0):
        if(yu>=0):
            print(*('Q',xu,yu))
            #yu-=1
            x=int(input())
            if(x==0):
                dj=0
                v.append(xu)
                v.append(yu)
            yu-=1
        else:
            xu-=1
            yu=100
    v.insert(0,'A')
    print(*v)
    xs=int(input())
    
        
    