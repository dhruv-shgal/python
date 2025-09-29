# search in a nearly sorted list
def srch_sorted(arr,target):
    l=0
    h=len(arr)-1
    while(l<=h):
        mid=l+h//2
        if arr[mid]==target:
            return mid
        if arr[mid-1]==target and mid>=l:
            return mid-1
        if arr[mid+1]==target and mid<=h:
            return mid+1
        if arr[mid]>target:
            h=mid-1
        else:
            l=mid+1
    return mid            



arr=[5,10,30,20,40]
target=20    
print(f"{target} is present at {srch_sorted(arr,target)}")