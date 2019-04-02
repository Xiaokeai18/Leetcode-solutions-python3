class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1,-1]
        index_l = 0
        index_r = len(nums)-1
        
        index,index_l,index_r = self.find(nums,target,index_l,index_r,'locate')
        if index == -1:
            return [-1,-1]
        return [self.find(nums,target,index_l,index,'left') , self.find(nums,target,index,index_r,'right')]
        
    def find(self,nums,target,index_l,index_r,mode):   
        if mode == 'locate':
            index = (index_l + index_r)>>1
            while(nums[index] != target):
                if index == index_l or index == index_r:
                    if nums[index_r] != target:
                        return [-1,-1,-1]
                if nums[index] > target:
                    index_r = index
                    index = (index_l + index_r)>>1
                else:
                    index_l = index
                    if index == index_r-1:
                        index = index_r
                    else:
                        index = (index_l + index_r)>>1
            return index,index_l,index_r
        
        elif mode  == 'left':
            index = index_r
            if index == index_l:
                return index
            while(nums[index-1] == target or nums[index] != target):
                if nums[index] == target:
                    index_r = index
                else:
                    index_l = index
                index = (index_l + index_r)>>1
                if index == 0:
                    return 0
            return index
        elif mode == 'right':
            index = index_l
            if index == index_r:
                return index
            while(nums[index+1] == target or nums[index] != target):
                if nums[index] == target:
                    index_l = index
                    if index == index_r-1:
                        index = index_r
                    else:
                        index = (index_l + index_r)>>1
                else:
                    index_r = index
                    index = (index_l + index_r)>>1
                if index == len(nums)-1:
                    return index
            return index
