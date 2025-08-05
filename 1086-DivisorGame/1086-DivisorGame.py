# Last updated: 8/5/2025, 2:55:50 PM
class Solution:
    def __init__(self):
        self.turn = "Alice"
    def divisorGame(self, N):
        if N == 1 and self.turn == "Alice":
            return False
        elif N == 1 and self.turn == "Bob":
            return True
        else:
            if self.turn == "Alice":
                self.turn = "Bob"
            else:
                self.turn = "Alice"
            return self.divisorGame(N-1)
        