def print_factors(N):
   # This function takes a number and prints the factors

  # print("The factors of",x,"are:")
   for i in range(1, N + 1):
       if N % i == 0:
           print(i)

# change this value for a different result.
#num = 320

# uncomment the following line to take input from the user
N = int(input())

print_factors(N)
