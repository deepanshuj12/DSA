class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        minn=float('infinity')
        nums.sort()
        j=k-1
        lent=len(nums)
        for i in range (lent):
            if j>len(nums)-1:
                break
            minn=min(minn,nums[j]-nums[i])
            j=j+1
        return minn