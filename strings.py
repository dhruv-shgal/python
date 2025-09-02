# def no_of_vowels(str1):
#     str1=str1.lower()
#     count=0
#     for char in str1:
#         if char in 'aeiou':
#             count += 1
#     return count
# str1="Python Programming"
# print(no_of_vowels(str1))

# def equal_strings(str1, str2):
#     i = 0
#     j = 0

#     while i < len(str1) and j < len(str2):
#         if str1[i] != str2[j]:
#             return False
#         i += 1
#         j += 1

   
#     if i != len(str1) or j != len(str2):
#         return False

#     return True


# s = "hello"
# t = "world"
# print(equal_strings(s, t)) 

# def palindrome(s):
#     return s==s[::-1]
# s= "Hello, World!"
# s="".join(s.split())
# s=s.lower()
# print(palindrome(s))

# def count_words(s):
# #     s="".join(s.split())
# #     s=s.lower()
#     words = s.split()
#     return len(words)
# s = "Hello, World! Welcome to Python programming."
# print(count_words(s))

def remove_duplicates(s):
    lst=[]
    for i in s:
        if i not in lst:
            lst.append(i)
    return "".join(lst)


s="Hello, World!"
print(remove_duplicates(s))