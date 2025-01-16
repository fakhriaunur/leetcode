from typing import List


def meeting_rooms(intervals: List[List[int]]) -> bool:
    intervals.sort()

    for i in range(1, len(intervals)):
        prev = intervals[i - 1]
        curr = intervals[i]

        if prev[1] > curr[0]:
            return False

    return True


if __name__ == "__main__":
    intervals = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = meeting_rooms(intervals)
    print("true" if res else "false")
