def findMedianSortedArrays(scoresA, scoresB):
    m, n = len(scoresA), len(scoresB)
    total = m + n

    i = j = 0
    count = 0
    prev = curr = 0

    while count <= total // 2:
        prev = curr

        if i < m and (j >= n or scoresA[i] <= scoresB[j]):
            curr = scoresA[i]
            i += 1
        else:
            curr = scoresB[j]
            j += 1

        count += 1

    # If total elements are even
    if total % 2 == 0:
        return (prev + curr) / 2.0
    else:
        return float(curr)

print(findMedianSortedArrays([1,3],[2]))
