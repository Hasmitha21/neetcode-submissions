class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # BRUTE FORCE
        allnums = []
        for i in range(len(nums1)):
            allnums.append(nums1[i])
        
        for i in range(len(nums2)):
            allnums.append(nums2[i])
        
        allnums.sort()
        l = 0
        r = len(allnums)
        if r%2 != 0:
            return allnums[r//2]
        else:
            mid1 = allnums[(r // 2) - 1]
            mid2 = allnums[r // 2]
            return  (mid1+mid2) /2