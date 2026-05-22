def aggressive_cows(stalls, k):
    stalls.sort()
    # Check if we can place all cows with at least 'dist' separation
    def can_place(dist):
        cows = 1
        last_pos = stalls[0]

        for i in range(1, len(stalls)):
            if stalls[i] - last_pos >= dist:
                cows += 1
                last_pos = stalls[i]
                if cows == k:
                    return True
        return False

    low, high = 1, stalls[-1] - stalls[0]
    best = 0

    while low <= high:
        mid = (low + high) // 2

        if can_place(mid):
            best = mid          # mid is possible → try bigger
            low = mid + 1
        else:
            high = mid - 1      # mid not possible → try smaller

    return best


        
