n=int(input())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
count=0
for i in range(n):
  if(l[i] in k):
    count=count+1
if(count==n):
  print("yes")
else:
  print("no")
