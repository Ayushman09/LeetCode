def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = len(nums)-1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0:   # nums are in descending order
            nums.reverse()
            return
        k = i - 1    # find the last "ascending" position
        while nums[j] <= nums[k]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]  
        l, r = k+1, len(nums)-1  # reverse the second part
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l +=1 ; r -= 1

#new soln using binary search
def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1

        # use binary search because it's descending order
        if i > 0:
            left, right = i, n - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[i-1] < nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            nums[i-1], nums[left-1] = nums[left-1], nums[i-1]

        # reverse
        left, right = i, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1