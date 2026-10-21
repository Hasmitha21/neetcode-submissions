class KthLargest:

    def __init__(self, k: int, nums: List[int]):


        # self.k = k
        # self.arr = nums

        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        return self.minHeap[0]

        #SORTING
        # self.arr.append(val)
        # self.arr.sort()
        # return self.arr[len(self.arr) - self.k]
