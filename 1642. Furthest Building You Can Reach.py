def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ladder = [0 for _ in range(ladders)]
        for i in range(1, len(heights)):
            curr = heights[i] - heights[i-1]
            if curr > 0:
                heapq.heappush(ladder, curr)
                bricks -= heapq.heappop(ladder)                    
            if bricks < 0:
                return i-1
        return len(heights) -1 