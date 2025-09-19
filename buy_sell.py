prices = [7,1,5,3,6,4]
l=0
r=1
maxprofit=0
while(r<len(prices)):
    if prices[l] < prices[r]:
        profit=prices[r]-prices[l]
        maxprofit=max(profit,maxprofit)
    else:
        l+=1
    r+=1
print(f"the maximum profit is {maxprofit}")        


       