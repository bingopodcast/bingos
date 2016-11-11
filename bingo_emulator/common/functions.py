def count_seq(nums):
    last = nums[0]
    max_hits = 0
    hits = 0

    for i in nums:
        if last == i - 1 or last == i:
            hits += 1
            if max_hits < hits:
                max_hits = hits
        else:
            hits = 1
        last = i

    return max_hits
