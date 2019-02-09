class Solution:
    def reverse(self, nums, start, end):
        i = start
        j = end
        while i < j:
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            i += 1
            j -= 1
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k %= l
        self.reverse(nums, 0, l-1)
        self.reverse(nums, 0, k -1)
        self.reverse(nums, k, l-1)