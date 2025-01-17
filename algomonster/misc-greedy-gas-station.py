from typing import List


def starting_station(gas: List[int], dist: List[int]) -> int:
    n = len(gas)
    curr_start = None
    curr_gas = 0
    curr_loc = 0

    while curr_loc < n * 2:
        if not curr_start:
            curr_start = curr_loc

        curr_gas += gas[curr_loc % n]
        curr_gas -= dist[curr_loc % n]

        if curr_gas < 0:
            curr_start = None
            curr_gas = 0

        curr_loc += 1

        if curr_start and curr_loc - curr_start == n:
            return curr_start % n

    return -1


if __name__ == "__main__":
    gas = [int(x) for x in input().split()]
    dist = [int(x) for x in input().split()]
    res = starting_station(gas, dist)
    print(res)
