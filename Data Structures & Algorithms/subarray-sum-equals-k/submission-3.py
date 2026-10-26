class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # res = 0
        # for i in range(len(nums)):
        #     sum = 0
        #     for j in range(i, len(nums)):
        #         sum += nums[j]
        #         if sum == k:
        #             res += 1
        # return res

        count = 0
        prefixSums = {0 : 1}
        sum = 0

        for num in nums:
            sum += num
            diff = sum - k
            count += prefixSums.get(diff,0)
            prefixSums[sum] = 1 + prefixSums.get(sum,0)
        
        return count