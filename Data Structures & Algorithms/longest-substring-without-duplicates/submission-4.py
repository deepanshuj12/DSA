class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j=0,0
        temp=''
        lent=len(s)
        maxx=0
        while j<lent:
            while s[j] in temp:
                temp = temp[1:]
                i=i+1
            temp=temp+s[j]
            maxx=max(maxx,len(temp))
            j=j+1
        return maxx