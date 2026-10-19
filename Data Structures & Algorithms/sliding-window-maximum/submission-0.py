class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # BRUTE FORCE O(n * k)

        # output = []

        # for i in range(len(nums)-k+1):
        #     maxnum = nums[i]
        #     for j in range(i, i+k):
        #         maxnum = max(maxnum, nums[j])
        #     output.append(maxnum)
        
        # return output


        # -- MONOTONIC QUEUE --

        output = []
        q = collections.deque()
        l =0
        r = 0
        while r<len(nums):
            # pop smaller value from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left val from window
            if l > q[0]:
                q.popleft()
            
            if (r - l+1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        
        return output