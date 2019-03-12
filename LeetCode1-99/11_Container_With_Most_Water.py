class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        opt = 0
        if len(height) <= 1:
            return 0
        left = 0
        right = len(height) - 1
        while(left < right):
            if height[left] <= height[right]:
                opt = max(opt,(right-left)*height[left])
                left += 1
            else:
                opt = max(opt,(right-left)*height[right])
                right -= 1
        return opt
