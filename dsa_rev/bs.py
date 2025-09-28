def last_occ(arr,target):
    l=0
    h=len(arr)-1
    res=-1
    while l<=h:
        mid=(l+h)//2
        
        if arr[mid]==target:
            res=mid
            l=mid+1
        elif arr[mid]>target:
            h=mid-1
        else:
            l=mid+1                
    return res

def first_occ(arr,target):
    l=0
    h=len(arr)-1
    res=-1
    while l<=h:
        mid=(l+h)//2
        
        if arr[mid]==target:
            res=mid
            h=mid-1
        elif arr[mid]>target:
            h=mid-1
        else:
            l=mid+1                
    return res


arr=[2,4,10,10,10,18,20]
target=10
print(f"the first {target} appears at {first_occ(arr,target)} and the last {target} occurs at {last_occ(arr,target)}")