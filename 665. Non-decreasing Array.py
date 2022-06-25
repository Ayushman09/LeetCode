def checkPossibility(self, nums: List[int]) -> bool:
        p, n = -1, len(nums)
        for i in range(n - 1):
            if nums[i] > nums[i+1]:
                if p != -1: return False
                p = i
        return p in [-1, 0, n-2] or nums[p-1] <= nums[p+1] or nums[p] <= nums[p+2]