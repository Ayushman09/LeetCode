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

#greedy approach
def twoCitySchedCost(self, costs: List[List[int]]) -> int:
    # If all the people travels to the cityA then total cost:
    totalA = 0
    for costA, _ in costs:
        totalA += costA
        
    # If all the people wish to travel to cityB instead of cityA then the difference in cost would be:
    difference = [costB-costA for costA, costB in costs]
        
    """
        Since in both the cities the number of people travelling should be equal and their total cost should be minimum,
        So if we move half of the people from cityA to cityB having minimum difference among all the people then the total cost would be the minimum.
    """
    # Total cost of people travelling to cityB instead of cityA having minimum difference:
    totalB = sum(sorted(difference)[:len(costs)//2])
    return totalA + totalB   