class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        sumz=0
        bound=1
        cost.sort(reverse=True) #sort
        for i in range(len(cost)):
            if bound==3:
                bound=1
                continue
            sumz=sumz+cost[i]
            bound=bound+1
        return sumz