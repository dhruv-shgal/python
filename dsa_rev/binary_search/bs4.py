#floor of an element
def floor(lst,key):
    l=0
    h=len(lst)-1
    while(l<=h):
        mid = (l+h)//2
        if lst[mid]==key:
            return lst[mid]
        if lst[mid]>key:
            h=mid-1
        else:
            res=mid
            l=mid+1
    return lst[res]    
                
lst=[1,2,3,4,8,10,10,12,19]
key=125
print(floor(lst,key))