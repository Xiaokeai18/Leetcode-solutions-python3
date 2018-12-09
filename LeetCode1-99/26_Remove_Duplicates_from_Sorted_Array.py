class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        else:
            j=0
            for i in range(len(nums)):
                if nums[i] != nums[j]:
                    j+=1
                    nums[j] = nums[i]
            return j+1        