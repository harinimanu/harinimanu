def checkValidity(a, b, c):  
      
    # check condition  
    if (a + b <= c) or (a + c <= b) or (b + c <= a) : 
        print("yes")
    else: 
        print("no")        
  
# driver code  
a = 7
b = 10
c = 5
print(checkValidity(a, b, c)) 
