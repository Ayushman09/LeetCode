#leetcode HARD
#cleanest binary search solution
def splitArray(self, nums: List[int], m: int) -> int:
        def can_split(x: int) -> bool:
            curr, cuts = 0, 0
            for num in nums:
                if num + curr > x:
                    cuts, curr = cuts + 1, 0
                curr += num
            return cuts < m

        left, right = max(nums), sum(nums)
        while left < right:
            mid = left + (right - left) // 2
            if can_split(mid):
                right = mid
            else:
                left = mid + 1
        return left