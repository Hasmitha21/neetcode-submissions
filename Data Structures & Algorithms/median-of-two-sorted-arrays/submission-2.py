class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # BRUTE FORCE O(m+n)(log m+n)
        # allnums = []
        # for i in range(len(nums1)):
        #     allnums.append(nums1[i])
        
        # for i in range(len(nums2)):
        #     allnums.append(nums2[i])
        
        # allnums.sort()
        # l = 0
        # r = len(allnums)
        # if r%2 != 0:
        #     return allnums[r//2]
        # else:
        #     mid1 = allnums[(r // 2) - 1]
        #     mid2 = allnums[r // 2]
        #     return  (mid1+mid2) /2

        A = nums1
        B = nums2
        if len(A) > len(B):
            A,B = B, A
        #keeping A smaller 

        totallen = len(A) + len(B)
        half = totallen // 2
        l = 0
        r = len(A) - 1
        while True:
            A_mid = (l + r) // 2 # A
            B_left_index = half - A_mid - 2 # B

            Aleft = A[A_mid] if A_mid >=0 else float("-inf")
            Aright = A[A_mid + 1] if A_mid+1 < len(A) else float("inf")
            Bleft = B[B_left_index] if B_left_index >=0 else float("-inf")
            Bright = B[B_left_index + 1] if B_left_index+1 < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if totallen % 2 != 0:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft,Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = A_mid - 1
            else:
                l = A_mid + 1