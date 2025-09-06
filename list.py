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

# def plusone(lst):
#     lst=lst[::-1]
#     one,i=1,0
#     while one:
#         if i<len(lst):
#             if lst[i]==9:
#                 lst[i]=0
#             else:    
#                 lst[i]+=1
#                 one=0
#         else:
#             lst.append(1)
#             one=0
#         i+=1    
#     return lst[::-1]                

# lst=[5,9,9,9]
# print(plusone(lst))


# def find_missing_number(nums):
#     xor1,xor2=0,0
#     n=len(nums)-1
#     for i in range(n):
#         xor2=xor2^nums[i]
#         xor1=xor1^(i+1)
#     xor1=xor1^n
#     return xor1^xor2    
# nums = [3, 0, 1]
# print(find_missing_number(nums))

# def is_sorted(arr):
#     return sorted(arr)==arr


# arr = [1, 2, 3, 4, 5]
# print(is_sorted(arr))


def move_zeroes(nums):
    j=0
    for i in range(len(nums)):
        if nums[i]!=0:
           nums[i],nums[j]=nums[j],nums[i]
           j+=1
    return nums           
nums = [0, 1, 0, 3, 12]
print(move_zeroes(nums))