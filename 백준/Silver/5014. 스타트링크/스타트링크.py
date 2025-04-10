from collections import deque  

F, S, G, U, D = map(int, input().split())  
visited = [0]*(F+1)

def bfs():  
    deq = deque()  
    deq.append(S)  

    visited[S] = 1  

    while deq:  
        current = deq.popleft()  

        if current == G:  
            return visited[current] - 1  
        else:  
            for x in (current + U, current - D):  
                if (0 < x <= F) and visited[x] == 0:  
                    visited[x] = visited[current] + 1  
                    deq.append(x)  

    return "use the stairs"  

print(bfs())