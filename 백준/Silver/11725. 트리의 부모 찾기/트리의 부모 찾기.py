import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [[] for i in range(N+1)]
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
queue.append(1)

visited = [0]*(N+1)

def bfs():
    while queue:
        now = queue.popleft()
        for next in graph[now]:
            if visited[next] == 0:
                visited[next] = now
                queue.append(next)

bfs()
answer = visited[2:]
for x in answer:
    print(x)