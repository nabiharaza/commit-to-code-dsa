# Last updated: 8/5/2025, 2:57:04 PM
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A)!=len(B):
            return False
        head = 0
        while True:
            if A == B:
                return True
            else:
                A = A[1: len(A)] + A[0]
                if head == 0:
                    head = len(A) - 1
                else:
                    head -= 1
            if head == 0:
                break
        return False