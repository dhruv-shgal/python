def is_palindrome(lst):
    return lst==lst[::-1]



lst=[7,8,9,8,6]    
print(is_palindrome(lst))