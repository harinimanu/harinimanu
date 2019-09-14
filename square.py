a,b=map(int,input().split())
b,c=map(int,input().split())
c,d=map(int,input().split())
d,a=map(int,input().split())
if(a**2-c**2==b**2-d**2):
    print("yes")
else:
    print("no")
