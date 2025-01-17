from typing import List


def merge(left: List[List[int]], right: List[List[int]]) -> List[List[int]]:
    res: List[List[int]] = []

    def update(x: int, y: int):
        if not res or (res[-1][0] != x and res[-1][1] != y):
            res.append([x, y])

        else:
            res[-1][1] = y

    currx, curry = 0, 0
    i1, i2 = 0, 0
    ly, ry = 0, 0

    while i1 < len(left) and i2 < len(right):
        x1, y1 = left[i1]
        x2, y2 = right[i2]

        if x1 < x2:
            i1 += 1
            ly = y1

        else:
            i2 += 1
            ry = y2

        currx = min(x1, x2)
        curry = max(ly, ry)
        update(currx, curry)

    while i1 < len(left):
        x1, y1 = left[i1]
        i1 += 1
        update(x1, y1)

    while i2 < len(right):
        x2, y2 = right[i2]
        i2 += 1
        update(x2, y2)

    return res


def get_skyline(buildings: List[List[int]]) -> List[List[int]]:
    n = len(buildings)

    if n == 0:
        return []

    if n == 1:
        return [
            [buildings[0][0], buildings[0][2]],
            [buildings[0][1], 0],
        ]

    left_bs = get_skyline(buildings[: n // 2])
    right_bs = get_skyline(buildings[n // 2 :])

    return merge(left_bs, right_bs)


if __name__ == "__main__":
    buildings = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = get_skyline(buildings)
    for row in res:
        print(" ".join(map(str, row)))
