n=int(input())
arr = list(map(int,input().split()))
l=[]  
for i in range(0, len(arr)):  
    for j in range(i+1, len(arr)):  
        if(arr[i] == arr[j]):  
            l.append(arr[j])
for i in range(len(l)):
    print(l[i],end=" ")
if(len(l)==0):
    print(-1)
