def dec_to_binary(n):
    if n<0:
        n=-n
        return '-'+ dec_to_binary(n // 2) + str(n % 2)
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return dec_to_binary(n // 2) + str(n % 2)
        
n=-5
print(dec_to_binary(n))  # Output: 101