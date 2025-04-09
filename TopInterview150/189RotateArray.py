class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums) # Get the length of the input list
        k = k%n # Check for the cases where k is greater than n, so we take the remainder
        nums[:] = nums[-k:] + nums[:-k] # Reorganizing the list of numbers by slicing the list into two parts and concatenating them