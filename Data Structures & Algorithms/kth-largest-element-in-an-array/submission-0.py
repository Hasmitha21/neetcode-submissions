class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k_largest_nums = heapq.nlargest(k,nums)
        return k_largest_nums[-1]