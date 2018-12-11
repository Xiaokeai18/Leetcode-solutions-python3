class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index = 0
        for number in nums:
            if number < target:
                index += 1
            else:
                return index
        return index