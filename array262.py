n,k=map(int,input().split())
l=list(map(int,input().split()))
m=[]
def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 
for i in l:
  c=l.count(i)
  if(c==k):
    m.append(i)
h=sorted(m)
if(len(m)!=0):
  h=Remove(h)
  for i in h:
    print(i,end=" ")
else:
  print(-1)

