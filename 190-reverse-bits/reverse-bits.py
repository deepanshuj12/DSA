# class Solution:
#     def reverseBits(self, n: int) -> int:
#         binary="{:032b}".format(n)
#         binary=bin(binary)[2:]
#         res=0
#         newbin=0
#         for i in range(32):
#             res=binary%10
#             newbin=newbin*10+res
#             binary=binary//10
#         return  newbin
class Solution:
    def reverseBits(self, n: int) -> int:
        binary = "{:032b}".format(n)
        reversed_binary = binary[::-1]
        return int(reversed_binary, 2)