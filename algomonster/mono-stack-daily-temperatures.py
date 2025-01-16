from typing import List


def daily_temperatures(t: List[int]) -> List[int]:
    stack = []
    res = [0] * len(t)

    for i in range(len(t)):
        # stack is not empty and current temp is warmer
        while stack and t[i] > t[stack[-1]]:
            prev_day_index = stack.pop()
            res[prev_day_index] = i - prev_day_index

        stack.append(i)

    return res


if __name__ == "__main__":
    t = [int(x) for x in input().split()]
    res = daily_temperatures(t)
    print(" ".join(map(str, res)))
