# def cel_to_fah(celsius):
#     f=(9/5 * celsius)+32
#     return f


def rounds_lift(n,c) :
    if n//c==0:
        return n//c
    else: 
        return n//c + 1
print(rounds_lift(7,4)) 