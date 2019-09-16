n=int(input())
b=str(n)
a=len(b)
sumis=0
for i in range(a-2,a):
  c=int(b[i])
  sumis=sumis+c
if(sumis%4==0):
  print("Yes")
else:
  print("No")
