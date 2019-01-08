class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        prev = nums[0]-1 #只要保证prev不等于nums[0]就行了
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
               prev = nums[i]
            else:
                if prev != nums[i-1]:
                    return nums[i-1]
        return nums[-1]