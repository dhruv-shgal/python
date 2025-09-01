# def dec_to_binary(n):
#     if n<0:
#         n=-n
#         return '-'+ dec_to_binary(n // 2) + str(n % 2)
#     if n == 0:
#         return "0"
#     elif n == 1:
#         return "1"
#     else:
#         return dec_to_binary(n // 2) + str(n % 2)
        
# n=-5
# print(dec_to_binary(n))  # Output: 101
# def binary_to_dec(n):
#     if n[0] == '-':
#         return -binary_to_dec(n[1:])
#     elif n == "0":
#         return 0
#     elif n == "1":
#         return 1
#     else:
#         return 2 * binary_to_dec(n[:-1]) + int(n[-1])

# def binary_to_dec_iter(n):
#     if n[0] == '-':   # handle negative numbers
#         return -binary_to_dec_iter(n[1:])

#     decimal = 0
#     for digit in n:
#         decimal = decimal * 2 + int(digit)
#     return decimal


# # Example
# n = '101'
# print(binary_to_dec_iter(n))  # Output: 5

# n='101'
# print(binary_to_dec(n))  # Output: 5
# print(n[:-1]+int(n[-1]))
# print(int(n[-1]))

def gcd(n, m):
 
    if n < 0:
        n = -n
    if m < 0:
        m = -m


    if n == 0 and m == 0:
        return 0

    
    while m != 0:
        n, m = m, n % m
    return n

