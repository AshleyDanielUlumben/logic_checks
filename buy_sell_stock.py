# Buy and Sell Stock

def buySellStock(prices):
        
    # Using the 2-pointer solution
    # left pointer -> buying
    # right pointer -> selling
    l, r = 0, 1 

    # Just using a variable to store the max profit
    maxProfit = 0

    # Buy low and Sell high
    # only need to go through the list once
    while r < len(prices):
        if prices[l] < prices[r]:
            Profit = prices[r] - prices[l]
            maxProfit = max(maxProfit, Profit)
        else:
            l = r 
        r += 1
    
    return maxProfit


stocklist = [7,1,5,3,6,4]
print(buySellStock(stocklist))