n = int(input())

for _ in range(n):
    count , S = input().split()
    for i in S:
        print(i*int(count), end='')
    print()