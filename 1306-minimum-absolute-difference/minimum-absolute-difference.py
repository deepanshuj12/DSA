class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        k=1
        minn=float('inf')
        lent=len(arr)
        nums=[]
        for i in range(lent):
            if k>lent-1:
                break
            minn= min(minn,arr[k]-arr[i])
            k=k+1
        k=1
        for i in range(lent):
            if k>lent-1:
                break
            if arr[k]-arr[i]==minn:
                nums.append([arr[i],arr[k]])
            k=k+1
        return nums