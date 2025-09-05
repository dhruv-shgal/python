# def is_palindrome(lst):
#     return lst==lst[::-1]



# lst=[7,8,9,8,6]    
# print(is_palindrome(lst))

def rotate_array(arr,d):
    arr=arr[d:]+arr[:d]
    d = d % len(arr)
    arr = arr[-d:] + arr[:-d]
    return arr
arr=[1, 2, 3, 4, 5]
d=2
print(rotate_array(arr,d))


