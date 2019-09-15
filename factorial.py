n=int(input())
def factorial(n):
    if(n==1):
        print(n)
    else:
        print(n*factorial(n-1))
factorial(n)
