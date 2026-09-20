def maxProfit(self, prices: list[int]) -> int:
    if len(prices)<=1:
        return 0
    pro=0
    minprice=prices[0]
    for i in prices[1:]:
        if i<minprice:
            minprice=i
        if i-minprice>pro:
            pro=i-minprice
    return pro