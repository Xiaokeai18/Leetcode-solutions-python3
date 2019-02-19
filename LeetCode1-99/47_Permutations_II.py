class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums==[]: return [[]]
        opt=[]
        nums.sort()
        self.core(nums,opt,[])
        return opt

    def core(self,nums,opt,temp):
        if not len(nums):
            opt.append(temp)
            return 
        else:
            for i in range(len(nums)):
                if i>0 and nums[i]==nums[i-1]:
                    continue
                self.core(nums[:i]+nums[i+1:],opt,temp+[nums[i]])
