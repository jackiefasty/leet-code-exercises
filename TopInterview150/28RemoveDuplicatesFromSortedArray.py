class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=1
        for i in range(len(nums)):
            if nums[i] != nums[k-1]: # In case current element is not the same as previous, no duplication found
                nums[k] = nums[i] # Keep current element on new list iteration
                k+=1
        return k