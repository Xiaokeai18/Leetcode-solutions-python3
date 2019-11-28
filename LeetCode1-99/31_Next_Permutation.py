class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        index = len(nums) - 1
        while index > 0 and nums[index] <= nums[index-1]:
            index -= 1
        if index > 0:
            nums[index:] = nums[:index-1:-1]
            c1 = index - 1
            while nums[c1] >= nums[index]:
                index += 1
            temp = nums[c1]
            nums[c1] = nums[index]
            nums[index] = temp
        else:
            nums[:] = nums[::-1]