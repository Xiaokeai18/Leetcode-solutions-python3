class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum,max = 0,nums[0]
        for number in nums:
            if sum > 0:
                sum += number
            else:
                sum = number
            if sum > max:
                max = sum
            
        return max