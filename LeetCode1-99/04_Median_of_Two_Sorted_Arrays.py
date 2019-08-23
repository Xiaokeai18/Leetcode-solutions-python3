class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        def findk(nums1,nums2,k):
            #print(k)
            if nums1 == []:
                return nums2[k]
            if len(nums1) > len(nums2):
                return findk(nums2,nums1,k)
            if k == 0:
                return min(nums1[0],nums2[0])
            index = min(len(nums1)-1,k//2)

            if nums1[index] >= nums2[k//2]:
                if k == 1:
                    return findk(nums1,nums2[1:],0)
                nums2 = nums2[k//2:]
                k -= k//2
                return findk(nums1,nums2,k)
            elif nums1[index] < nums2[k//2]:
                if k == 1 or index == 0:
                    return findk(nums1[1:],nums2,k-1)
                nums1 = nums1[index:]
                k -= index
                return findk(nums1,nums2,k)

        k1 = (len(nums1) + len(nums2))//2
        k2 = (len(nums1) + len(nums2) - 1)//2
        
        if k1 == k2:
            return findk(nums1,nums2,k1)
        else:
            return float(findk(nums1,nums2,k1)+findk(nums1,nums2,k2))/2
