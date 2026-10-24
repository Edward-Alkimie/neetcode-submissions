class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 101
        max_value = 0

        for price in prices:
            if (price < min_price):
                min_price = price
                print(min_price)
            if price - min_price > max_value:
                max_value = price - min_price;
                print(max_value)

        return max_value

