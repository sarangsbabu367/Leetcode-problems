class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])
        merged_intervals = []
        curr_interval = intervals[0]
        
        for interval in intervals[1:]:
            if self._is_mergable(curr_interval, interval):
                curr_interval = [
                    curr_interval[0], max(curr_interval[1], interval[1])
                ]
            else:
                merged_intervals.append(curr_interval)
                curr_interval = interval
        merged_intervals.append(curr_interval)
        return merged_intervals

    @staticmethod
    def _is_mergable(start_interval, end_interval):
        return end_interval[0] <= start_interval[1]