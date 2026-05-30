from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        assert 1 <= len(prices) <= 10**5

        repere = prices
        repere.sort()
        repere.reverse()
        if prices == repere :
            return 0

        maxi = 0
        buy = False
        sell = False

        for i in range(len(prices)-1) :
            assert 0 <= prices[i] <= 10**4

        assert 0 <= prices[-1] <= 10**4

        return maxi

