n,k=map(int,input().split())
print("\n")
l=list(map(int,input().split()))
p=list(map(int,input().split()))
for j in range(0,k):
    l.append(p[j])
    print(max(l),end=" ")
