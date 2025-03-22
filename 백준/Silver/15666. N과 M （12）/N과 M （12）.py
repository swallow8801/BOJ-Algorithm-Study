def back_track(start, arr):
    if len(arr) == m:
        print(*arr)
        return

    for i in range(start, len(nums)):
        back_track(i, arr + [nums[i]])

n, m = map(int, input().split())
nums = sorted(set(map(int, input().split())))

back_track(0, [])