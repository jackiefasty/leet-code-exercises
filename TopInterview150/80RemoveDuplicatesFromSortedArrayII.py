class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            k = 0
        else:
            k = 1
            count = 1  # Count occurrences of the current number

            for i in range(1, len(nums)):
                if nums[i] == nums[k - 1] and count < 2:
                    nums[k] = nums[i]
                    k += 1
                    count += 1
                elif nums[i] != nums[k - 1]:
                    nums[k] = nums[i]
                    k += 1
                    count = 1
                elif nums[i] != nums[k-2]:
                    count = 1
            nums[:] = nums[:k]
        print(k, nums)