from typing import List


def multiply_matrix(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
    m = len(a)
    n = len(b)
    k = len(b[0])

    res = [[0] * k for _ in range(m)]

    for c in range(m):
        for r in range(n):
            a_entry = a[c][r]
            if a_entry == 0:
                continue

            for l in range(k):
                b_entry = b[r][l]
                res[c][l] += a_entry * b_entry

    return res


if __name__ == "__main__":
    a = [[int(x) for x in input().split()] for _ in range(int(input()))]
    b = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = multiply_matrix(a, b)
    for row in res:
        print(" ".join(map(str, row)))
