class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in range(len(letters)):
            if letters[i]>target:
                return letters[i]
        return letters[0]




        # term=''
        # for i in range(len(letters)):
        #     if ord(letters[i])>ord(target):
        #         term=letters[i]
        #         break
        # if term!='':
        #     return term
        # else:
        #     return letters[0]
