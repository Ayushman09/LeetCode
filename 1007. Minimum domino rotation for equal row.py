def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        ct = Counter(tops)
        cb = Counter(bottoms)
        
        num = 0
        for i in range(1, 7):
            if ct[i] + cb[i] >= len(tops):
                num = i
                break

        if num == 0:
            return -1
        
        for i in range(len(tops)):
            if tops[i] != num and bottoms[i] != num:
                return -1
            
        return min(len(tops) - tops.count(num), len(bottoms) - bottoms.count(num))