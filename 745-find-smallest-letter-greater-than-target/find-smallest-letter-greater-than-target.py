class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for j in range(len(letters)):
            if letters[j]>target:
                return letters[j]
        return letters[0]




        # term=''
        #
        # for i in range(len(letters)):
        #     if ord(letters[i])>ord(target):
        #         term=letters[i]
        #         break
        # if term!='':
        #     return term
        # else:
        #     return letters[0]
