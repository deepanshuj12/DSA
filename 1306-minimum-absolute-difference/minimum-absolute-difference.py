class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        minnn = min(arr[i + 1] - arr[i] for i in range(len(arr) - 1))

        return [
            [arr[i], arr[i + 1]]
            for i in range(len(arr) - 1)
            if arr[i + 1] - arr[i] == minnn
        ]
# class Solution:
#     def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
#         arr.sort()
#         k=1
#         minn=float('inf')
#         lent=len(arr)
#         nums=[]
#         for i in range(lent):
#             if k>lent-1:
#                 break
#             minn= min(minn,arr[k]-arr[i])
#             k=k+1
#         k=1
#         for i in range(lent):
#             if k>lent-1:
#                 break
#             if arr[k]-arr[i]==minn:
#                 nums.append([arr[i],arr[k]])
#             k=k+1
#         return nums