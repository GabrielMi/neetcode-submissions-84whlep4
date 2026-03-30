class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        l, r = 0, 1
        while l < r and r < len(intervals):
            if intervals[l][1] >= intervals[r][0]:
                intervals[l][1] = max(intervals[l][1], intervals[r][1])
                intervals.pop(r)
            else:
                l += 1
                r += 1
        return intervals
        
        [2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]

        [1,3],[2,2],[2,2],[2,3],[3,3],[4,6],[5,7]