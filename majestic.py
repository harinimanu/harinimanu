n = int(input())
a=list(map(int,input().split()))
if(a[0]+a[1]+a[2]==a[n-1]+a[n-2]+a[n-3]):
    print(1)
else:
    print(0)
