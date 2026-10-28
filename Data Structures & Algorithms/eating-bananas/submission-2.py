class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # time = dist/speed
        # hours = pile/speed
        # speed = 1
        # while True:
        #     time = 0
        #     for p in piles:
        #         time += math.ceil(p/speed)
            
        #     if time <= h:
        #         return speed
        #     speed += 1
        # return speed


        l = 1
        r = max(piles)
        res = r

        while l <= r:
            speed = (l+r) // 2
            time = 0
            for p in piles:
                time += math.ceil(p/speed)
            
            if time <= h:
                res = speed
                r = speed - 1
            else:
                l = speed + 1
        return res