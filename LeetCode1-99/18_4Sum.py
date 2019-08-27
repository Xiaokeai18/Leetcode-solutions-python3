class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        output = []
        length = len(nums)
        for i in range(length-3):
            if i==0 or nums[i-1]!=nums[i]:
                if nums[i] + sum(nums[i+1:i+4]) > target:
                    break
                if nums[i] + sum(nums[-1:-4:-1]) < target:
                    continue
                for j in range(i+1,length-2):
                    if j==i+1 or nums[j-1]!=nums[j]:
                        if nums[i] + nums[j] + sum(nums[j+1:j+3]) > target:
                            break
                        if nums[i] + nums[j] + sum(nums[-1:-3:-1]) < target:
                            continue
                        left = j + 1
                        right = length - 1
                        while left < right:
                            temp = nums[i] + nums[j] + nums[left] + nums[right]
                            if temp == target:
                                output.append([nums[i],nums[j],nums[left],nums[right]])
                                left += 1
                                right -= 1
                                while left < right and nums[left] == nums[left-1]:
                                    left += 1
                                while left < right and nums[right] == nums[right+1]:
                                    right -= 1
                            elif temp < target:
                                left += 1
                            else:
                                right -= 1
        return output