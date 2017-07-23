"""
122. Best Time to Buy and Sell Stock II
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as 
you like (ie, buy one and sell one share of the stock multiple times). However, you may not 
engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

解题思路：由于可以进行无限次的交易，那么只要是递增序列，就可以进行利润的累加。
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0  
        length = len(prices)  
        for i in range(0, length-1):  
            if prices[i+1] > prices[i]:  
                profit += prices[i+1] - prices[i]  
        return profit 