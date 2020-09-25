class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        x = {}
        for i,num in enumerate(nums):
            z = target - num
            if z not in x:
                x[num] = i
            else:
                return x[z],i
