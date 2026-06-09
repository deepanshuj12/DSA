class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # letters2=letters
        # letters2.append(target)
        app=False
        # flag=0
        term=''
        for i in range(len(letters)):
            uni=ord(letters[i])
            # if app==True:
            #     term=letters[i]
            #     # flag=1
            #     break
            if uni>ord(target):
                # app=True
                term=letters[i]
                break
        if term!='':
            return term
        else:
            return letters[0]
