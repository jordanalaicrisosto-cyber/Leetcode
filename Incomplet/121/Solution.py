from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        assert 1 <= len(prices) <= 10**5

        repere = prices[:]
        repere.sort()
        repere.reverse()

        if repere == prices :
            return 0

        maxi = 0
        buy = False
        sell = False
        print(prices, repere)
        for val in prices :
            assert 0 <= val <= 10**4
            if val == repere[-1] and not(buy):
                buy = True
            if val == repere[0] and buy and not(sell) :
                sell = True
                maxi = prices.index(val)
            if buy and sell :
                break

        assert 0 <= prices[-1] <= 10**4

        return maxi+1
