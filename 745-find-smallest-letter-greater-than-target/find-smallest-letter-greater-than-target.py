class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for r in range(len(letters)):
            if letters[r]>target:
                return letters[r]
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
