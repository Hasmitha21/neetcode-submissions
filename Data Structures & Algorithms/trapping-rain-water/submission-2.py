class Solution:
    def trap(self, height: List[int]) -> int:

        #TWO POINTERS
        # if not height:
        #     return 0
        
        # l = 0
        # r = len(height) -1

        # leftMax = height[l]
        # rightMax = height[r]
        # res = 0

        # while l < r:
        #     if leftMax < rightMax:
        #         l += 1
        #         leftMax = max(leftMax, height[l])
        #         res += leftMax - height[l]
        #     else:
        #         r -= 1
        #         rightMax = max(rightMax, height[r])
        #         res += rightMax - height[r]
        
        # return res
        
        # BRUTE FORCE
        # if not height:
        #     return 0
        
        # res = 0
        # for i in range(len(height)):
        #     leftMax = rightMax = height[i]

        #     for j in range(i):
        #         leftMax = max(leftMax, height[j])
            
        #     for j in range(i+1, len(height)):
        #         rightMax = max(rightMax, height[j])
            
        #     res += min(leftMax,rightMax) - height[i]
        
        # return res

        # PREFIX SUFFIX ARRAYS
        if len(height) == 0:
            return 0
        
        leftMax = [0] * len(height)
        rightMax = [0] * len(height)

        leftMax[0] = height[0]
        for i in range(1, len(height)):
            leftMax[i] = max(leftMax[i-1],height[i])
        
        rightMax[len(height)-1] = height[len(height)-1]
        for i in range(len(height)-2,-1,-1):
            rightMax[i] = max(rightMax[i+1],height[i])
        
        trapping = [0] * len(height)
        for i in range(len(height)):
            trapping.append(min(leftMax[i],rightMax[i])-height[i])
        
        sum = 0
        for i in range(len(trapping)):
            sum += trapping[i]
        
        return sum
        