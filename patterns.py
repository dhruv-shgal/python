n=int(input("enter the side of square"))

# DIAMOND PATTERN
# temp =0
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for k in range(2*i+1):
#         print("*",end="") 
#     print()    
    
# for i in range(n - 2, -1, -1):   # start from n-2 (to avoid repeating middle row)
#     # spaces
#     for j in range(n - i - 1):
#         print(" ", end="")
#     # stars
#     for k in range(2 * i + 1):
#         print("*", end="")
#     print() 

for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print()     

               
    

       