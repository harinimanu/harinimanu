n,m=map(int,input().split())
k=list(map(int,input().split()))
if m in k:
  print("yes",end=" ")
  print(k.count(m),end=" ")
else:
  print("no")
