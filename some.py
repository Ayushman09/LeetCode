# first, negate all weight values in-place
def lastStoneWeight(self, stones: List[int]) -> int:
        for i, s in enumerate(stones):
            stones[i] = -s
        heapify(stones)  # pass all negated values into the min-heap
        while stones:
            s1 = -heappop(stones)  # the heaviest stone
            if not stones:  # s1 is the remaining stone
                return s1
            s2 = -heappop(stones)  # the second-heaviest stone; s2 <= s1
            if s1 > s2:
                heappush(stones, s2-s1)  # push the NEGATED value of s1-s2; i.e., s2-s1
            # else s1 == s2; both stones are destroyed
        return 0  # if no more stones remain
