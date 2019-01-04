class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = {}
        
        for i in range(0,len(nums)):
            hash[nums[i]] = i
        for i in range(0,len(nums)):
            if (target-nums[i]) in hash :
                if hash.get(target-nums[i])!=i:
                    return [i,hash.get(target-nums[i])]