from typing import List


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    # sort by start time
    intervals.sort(key=lambda x: x[0])
    # include the earliest interval
    res: List[List[int]] = [intervals[0]]

    for interval in intervals[1:]:
        prev_start, prev_end = res[-1]
        curr_start, curr_end = interval

        # if x2 < y1 or y2 < x1:
        # x1 is the earliest, only need to compare the end time with the next start time interval
        if prev_end < curr_start:
            res.append(interval)
        else:
            # pick the bigger end time
            prev_end = max(prev_end, curr_end)
            res[-1][1] = prev_end

    return res


if __name__ == "__main__":
    intervals = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = merge_intervals(intervals)
    for row in res:
        print(" ".join(map(str, row)))
