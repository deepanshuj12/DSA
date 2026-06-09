class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        term=''
        for i in range(len(letters)):
            if ord(letters[i])>ord(target):
                term=letters[i]
                break
        if term!='':
            return term
        else:
            return letters[0]
