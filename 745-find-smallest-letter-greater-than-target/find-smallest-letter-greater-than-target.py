# class Solution:
#     def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
#         term=''
#         for i in range(len(letters)):
#             if ord(letters[i])>ord(target):
#                 term=letters[i]
#                 break
#         if term!='':
#             return term
#         else:
#             return letters[0]
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters)
        while left < right:
            mid = (left + right) // 2
            if letters[mid] > target:
                right = mid
            else:
                left = mid + 1
        if left == len(letters):
            return letters[0]
        return letters[left]