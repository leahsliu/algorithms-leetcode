class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # sliding window method
        l,r = 0, 1

        max_profit = 0


        while r < len(prices) :
            val1 = prices[l]
            val2 = prices[r]

            profit = val2 - val1
            if profit < 0:
                l = r

            if profit > max_profit:
                max_profit = profit
        
            r += 1

        return max_profit





s1 = Solution()
print("sol: 5, output: ", s1.maxProfit([7,1,5,3,6,4]))







