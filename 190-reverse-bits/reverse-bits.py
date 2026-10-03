
class Solution:
    def reverseBits(self, n: int) -> int:
        binary = "{:032b}".format(n)
        reversed_binary = binary[::-1]
        return int(reversed_binary, 2)
