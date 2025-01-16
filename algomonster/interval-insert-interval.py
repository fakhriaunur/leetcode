from typing import List


def insert_interval(
    intervals: List[List[int]], new_interval: List[int]
) -> List[List[int]]:
    intervals.append(new_interval)
    intervals.sort(key=lambda x: x[0])

    res = [intervals[0]]

    for interval in intervals[1:]:
        prev_start, prev_end = res[-1]
        curr_start, curr_end = interval

        if prev_end < curr_start:
            res.append(interval)

        else:
            prev_end = max(prev_end, curr_end)
            res[-1][1] = prev_end

    return res


if __name__ == "__main__":
    intervals = [[int(x) for x in input().split()] for _ in range(int(input()))]
    new_interval = [int(x) for x in input().split()]
    res = insert_interval(intervals, new_interval)
    for row in res:
        print(" ".join(map(str, row)))
