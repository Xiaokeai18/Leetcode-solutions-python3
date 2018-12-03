class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        mid = len(nums)>>1
        leftmax = self.maxSubArray(nums[:mid:])
        rightmax = self.maxSubArray(nums[mid::])
        crossmax = self.crossSubArray(nums,mid)
        return max(leftmax,rightmax,crossmax)
        
    def crossSubArray(self,array,middle):
        left,right = 0,0
        max = -float("Inf")
        for i in array[middle-1::-1]:
            left += i
            if left > max:
                max = left
        left = max
        max = -float("Inf")
        for i in array[middle::]:
            right += i
            if right > max:
                max = right
        return left + max