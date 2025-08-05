# Last updated: 8/5/2025, 2:56:28 PM
class StockSpanner:
    def __init__(self):
        self.stack = [] # pair of [price, ans]

    def next(self, price: int) -> int:
        ans = 1 
        while self.stack and self.stack[-1][0] <= price:
            ans += self.stack[-1][1]
            self.stack.pop()
        self.stack.append([price, ans])
        return ans


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)