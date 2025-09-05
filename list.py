# def is_palindrome(lst):
#     return lst==lst[::-1]



# lst=[7,8,9,8,6]    
# print(is_palindrome(lst))

# def rotate_array(arr,d):
#     # arr=arr[d:]+arr[:d]
#     # d = d % len(arr)
#     # arr = arr[-d:] + arr[:-d]
#     # return arr
#     return arr
# arr=[1, 2, 3, 4, 5]
# d=2
# print(rotate_array(arr,d))

def plusone(lst):
    lst=lst[::-1]
    one,i=1,0
    while one:
        if i<len(lst):
            if lst[i]==9:
                lst[i]=0
            else:    
                lst[i]+=1
                one=0
        else:
            lst.append(1)
            one=0
        i+=1    
    return lst[::-1]                

lst=[5,9,9,9]
print(plusone(lst))