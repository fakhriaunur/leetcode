def mergesort(arr: list[int]):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left_par = mergesort(arr[:mid])
    right_par = mergesort(arr[mid:])

    left = 0
    right = 0
    res = []

    while left < len(left_par) or right < len(right_par):
        if left >= len(left_par) or (
            right < len(right_par) and left_par[left] > right_par[right]
        ):
            res.append(right_par[right])
            right += 1

        else:
            res.append(left_par[left])
            left += 1

    return res
