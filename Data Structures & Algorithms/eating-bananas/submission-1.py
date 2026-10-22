class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # BRUTE FORCE O(M * N) - no of piles, max num of bananas in a pile

        # speed = 1
        # #time = dist/speed
        # # hours = pile/speed
        # while True:
        #     totalTime = 0
        #     for pile in piles:
        #         totalTime += math.ceil(pile/speed)
            
        #     if totalTime <= h:
        #         return speed
        #     speed +=1
        # return speed

        l = 1
        r = max(piles)
        # k = 1  to max(piles)
        res = r

        while l <= r:
            time = 0
            k = (l+r) //2
            for p in piles:
                time += math.ceil(p/k)
            if time <= h:
                r = k -1
                res = k
            else:
                l = k + 1
        return res
