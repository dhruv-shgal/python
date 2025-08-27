n=int(input("enter the side of square"))
temp =0
for i in range(n):
    for j in range(i):
        temp=temp+1
        print(temp, end=" ")
    print()    

       