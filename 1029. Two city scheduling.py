def twoCitySchedCost(self, costs: List[List[int]]) -> int:
     # Sorting the costs based on loss we will get i.e; cost[0] - cost[1]
    costs.sort(key = lambda cost: cost[0] - cost[1])
        
    left = 0
    right = len(costs) - 1
    minCost = 0
    # Adding first n cityA costs and last n cityB costs
    while left < right:
        minCost += costs[left][0] + costs[right][1]
        left += 1
        right -= 1 
    return minCost