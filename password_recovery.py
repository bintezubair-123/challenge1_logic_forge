def minWindow_bruteforce(log, pattern):
    if len(pattern) > len(log):
        return ""

    min_len = float("inf")
    result = ""

    for i in range(len(log)):
        for j in range(i, len(log)):
            sub = log[i:j+1]

            # Check if sub contains pattern
            freq = {}
            for c in sub:
                freq[c] = freq.get(c, 0) + 1

            valid = True
            for c in pattern:
                if freq.get(c, 0) < pattern.count(c):
                    valid = False
                    break

            if valid and len(sub) < min_len:
                min_len = len(sub)
                result = sub

    return result

print(minWindow_bruteforce("a", "a"))
