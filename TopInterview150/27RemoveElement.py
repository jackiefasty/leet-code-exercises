class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k=0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i] # Removing element in-place by reorganizing the list of numbers
                k+=1 # Increasing the number of elements in reorganized list of nums
        return k