class Solution(object):
    def permute(self, nums):
        if nums==[]: return [[]]
        outcome=[]
        self.core(nums,0,outcome)
        return outcome

    def core(self,nums,left,outcome):
        if left==len(nums)-1:
            outcome.append(nums[:])
            return 
        else:
            for i in range(left,len(nums)):
                if i==left:
                    self.core(nums,left+1,outcome)
                else:
                    nums[left],nums[i]=nums[i],nums[left]
                    self.core(nums,left+1,outcome)
                    nums[left],nums[i]=nums[i],nums[left]