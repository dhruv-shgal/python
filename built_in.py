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

# def max_consecutive_difference(lst):
#     max_diff=0
#     for i in range(1,len(lst)):
#         max_diff=max(abs(lst[i]-lst[i-1]),max_diff)
#     return max_diff

# lst = [1, 10, 3, 7, 5]
# print(max_consecutive_difference(lst))  

# def merge_sorted_list(lst1,lst2):
#     lst1.extend(lst2)
#     return sorted(lst1)
# lst1 = [1, 3, 5]
# lst2 = [2, 4, 6]
# mai=merge_sorted_list(lst1,lst2)
# final=list(dict.fromkeys(mai))
# print(final)

# def rotate_array(arr,d):
#     # arr=arr[d:]+arr[:d]
#     # d = d % len(arr)
#     arr = arr[-d:] + arr[:-d]
#     return arr
# arr=[1, 2, 3, 4, 5]
# d=2
# print(rotate_array(arr,d))

# def merge_dict(keys, values,main):
#     merged_dict = {**keys, **values,**main}
#     return merged_dict

# keys = {'a': 1, 'b': 2}
# values = {'c': 3, 'd': 4}
# main={'e': 5, 'f': 6}
# print(merge_dict(keys, values,main))

# def word_freq_count(lstr1):
    
#     word_count={}
#     for word in lstr1:
#         word=word.lower()

#         if word in word_count:
#             word_count[word]+=1
#         else:
#             word_count[word]=1
#     return word_count



# lstr1=['hello','world', 'hello']
# print(word_freq_count(lstr1))

def palindromic_tuplk(tup1):
    return tup1==tuple(reversed(tup1))


tup=(1, 2, 3, 4, 5)
print(palindromic_tuplk(tup))