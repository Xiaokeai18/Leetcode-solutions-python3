class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cache = nums[0]
        cnt = 0
        for num in nums:
            if cache == num:
                cnt += 1
            else:
                cnt -= 1
                if cnt <= 0:
                    cache = num
                    cnt = 1
        return cache