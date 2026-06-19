class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for z in range(len(letters)):
            if letters[z]>target:
                return letters[z]
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
