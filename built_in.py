# def sum_list(numbers):
#     total = 0
#     for n in numbers:
#         total += n
#     return total

# numbers = [1, 2, 2, 3, 4, 4, 5]
# # print(sum_list(numbers))
# print(set(list(numbers)))  # Built-in function to sum elements in an iterable

# def check_unque(num):
#     if num==set(num):
#         return True
#     return False
# numbers = [1, 2, 2, 3, 4, 4, 5]
# print(check_unque(numbers))

# numbers = [1, 2, 2, 3, 4, 4, 5]
# num=reversed(numbers)
# print(list(num))

# def count_even_odd(numbers):
#     cnt=0
#     cut=0
#     for n in numbers:
#         if n%2==0:
#             cnt+=1
#         else:
#             cut+=1 
#     return (cnt,cut)        
# print(count_even_odd([1,2,3,4,5,6,7,8,9]))

def max_consecutive_difference(lst):
    max_diff=0
    for i in range(1,len(lst)):
        max_diff=max(abs(lst[i]-lst[i-1]),max_diff)
    return max_diff

lst = [1, 10, 3, 7, 5]
print(max_consecutive_difference(lst))  