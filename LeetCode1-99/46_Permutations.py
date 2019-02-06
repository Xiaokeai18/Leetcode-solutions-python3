class Solution(object):
    def permute(self, nums):
        if nums==[]: return [[]]
        opt=[]
        self.generate(nums,0,opt)
        return opt

    def generate(self,nums,left,opt):
        if left==len(nums)-1:
            opt.append(nums[:])
            return 
        else:
            for i in range(left,len(nums)):
                if i==left:
                    self.generate(nums,left+1,opt)
                else:
                    nums[left],nums[i]=nums[i],nums[left]
                    self.generate(nums,left+1,opt)
                    nums[left],nums[i]=nums[i],nums[left]