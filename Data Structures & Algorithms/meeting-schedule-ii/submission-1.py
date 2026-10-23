"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        # 2 POINTERS
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res = 0
        count = 0
        s, e = 0,0
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        
        return res


        # if not intervals:
        #     return 0

        # rooms = 1
        # intervals.sort(key=lambda i:i.start)
        # lastEnd = intervals[0].end

        # for i in range(1,len(intervals)):
        #     if intervals[i].start < lastEnd:
        #         rooms += 1
        #     else:
        #         lastEnd = intervals[i].end
        
        # return rooms