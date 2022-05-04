def maxOperations(self, nums: List[int], k: int) -> int:
        cache = defaultdict(int)
        num_ops = 0
        for i in nums:
            if cache[i] > 0:
                cache[i] -= 1
                num_ops += 1
                continue
            cache[k-i] += 1
        return num_ops