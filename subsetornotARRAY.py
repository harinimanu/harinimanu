# Python 3 program to find whether an array 
# is subset of another array 
  
# Return 1 if arr2[] is a subset of  
# arr1[]  
def isSubset(arr1, arr2, m, n): 
    i = 0
    j = 0
    for i in range(n): 
        for j in range(m): 
            if(arr2[i] == arr1[j]): 
                break
          
        # If the above inner loop was 
        # not broken at all then arr2[i] 
        # is not present in arr1[]  
        if (j == m): 
            return 0
      
    # If we reach here then all 
    # elements of arr2[] are present 
    # in arr1[]  
    #return 1
  
 
n,m=map(int,input().split())  
arr1 = list(map(int,input().split())) 
arr2 = list(map(int,input().split()))  
  
m = len(arr1) 
n = len(arr2) 
  
if(isSubset(arr1, arr2, m, n)): 
    print("yes") 
else: 
    print("no")
