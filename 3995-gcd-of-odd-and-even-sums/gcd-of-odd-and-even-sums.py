class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        oddn=n*n
        evenn=n*(n+1)
        return evenn-oddn