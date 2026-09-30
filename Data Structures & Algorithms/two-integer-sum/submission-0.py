class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexMap = {}

        for i, n in enumerate(nums):
            indexMap[n] = i
        
        for i, n in enumerate(nums):
            complement = target - n
            if complement in indexMap and indexMap[complement] != i:
                return [i, indexMap[complement]]
        return []