#BUBBLE SORT
# l1=[5,4,3,2,1]
# for j in range(len(l1)-1):
#     for i in range(1,len(l1)-j):
#         if l1[i]<l1[i-1]:
#             l1[i],l1[i-1]=l1[i-1],l1[i]
# print(l1)

#SELECTION SORT
# lst1=[9,13,20,24,46,52]
# for i in range(len(lst1)-2):
#     mini=i
#     for  j in range(i,len(lst1)):
#         if lst1[j]<lst1[mini]:
#             mini=j
#     lst1[i],lst1[mini]=lst1[mini],lst1[i]
# print(lst1)    

def insertion_sort(lst1):
    for i in range(len(lst1)):
        j=i
        while(j>0 and lst1[j-1]>lst1[j]):
            lst1[j-1],lst1[j]=lst1[j],lst1[j-1]
            j-=1
    return lst1        


lst1=[12 ,25 ,11 ,34 ,90,22]
print(insertion_sort(lst1))