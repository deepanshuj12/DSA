class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        arr=[]
        
        for i in range(1,10):
            num=0
            for k in range(i,10):
                num= num*10+ k
                if num>=low and num<=high:
                    arr.append(num)
        return sorted(arr)