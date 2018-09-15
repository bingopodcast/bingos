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

def woodrail_search(s):
    s.sound.stop_music()
    if s.ball_count.position == 1:
        s.sound.play_music('search1', -1)
    if s.ball_count.position == 2:
        s.sound.play_music('search2', -1)
    if s.ball_count.position == 3:
        s.sound.play_music('search3', -1)
    if s.ball_count.position == 4:
        s.sound.play_music('search4', -1)
    if s.ball_count.position == 5:
        s.sound.play_music('search5', -1)
    if s.ball_count.position == 6:
        s.sound.play_music('search6', -1)
    if s.ball_count.position == 7:
        s.sound.play_music('search7', -1)
    if s.ball_count.position == 8:
        s.sound.play_music('search8', -1)
