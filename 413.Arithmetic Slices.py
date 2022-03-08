from functools import cache

def numberOfArithmeticSlices(nums) -> int:
        @cache
        def count(n):
            if cnt < 3: return 0
            return n - 2 + count(n - 1)
        
        prev, cnt, ans = None, 2, 0
        for i in range(1, len(nums)):
            diff = nums[i-1] - nums[i]
            if diff == prev:
                cnt += 1
            else:
                ans += count(cnt)
                cnt = 2
                
            prev = diff
            
        return ans + count(cnt)