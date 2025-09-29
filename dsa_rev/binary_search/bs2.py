def no_sorted(arr):
    l=0
    n=len(arr)
    h=len(arr)-1
    while l<=h:
        if arr[l] <= arr[h]:
            return l
        mid=(l+h)//2
        next=(mid+1)%n
        prev=(mid+n-1)%n
        if arr[mid]<=arr[prev] and arr[mid]<=arr[next]:
            return mid
        if arr[l]<=arr[mid]:
            l=mid+1
        else:
            h=mid-1
    return -1
arr=[11,12,13,18,2,5,6,8]
print(no_sorted(arr))
