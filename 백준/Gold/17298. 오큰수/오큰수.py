import sys

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
answer = [-1] * N
stack = []

for i in range(N):
    while stack and num_list[stack[-1]] < num_list[i]:
        idx = stack.pop()
        answer[idx] = num_list[i]
    stack.append(i)

print(*answer)
