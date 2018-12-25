class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums_hash = {}
        result = []
        for num in nums:
            nums_hash[num] = nums_hash.get(num, 0) + 1
        if 0 in nums_hash and nums_hash[0] >= 3:
            result.append([0, 0, 0])
        #分别筛选出正和负的值
        neg = list(filter(lambda x: x < 0, nums_hash))
        pos = list(filter(lambda x: x>= 0, nums_hash))
        for i in neg:
            for j in pos:
                dif = 0 - i - j
                if dif in nums_hash:
                    if dif in (i, j) and nums_hash[dif] >= 2:
                        result.append([i, j, dif])
                    if dif < i or dif > j:
                        result.append([i, j, dif])                   
        return result