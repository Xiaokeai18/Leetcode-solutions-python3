class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        number = 1
        if 1 in nums:
            nums.sort()
            one = nums.index(1)
            for i in range(one,len(nums)):
                if number == nums[i]:
                    number +=1               
            return number
        else:
            return 1