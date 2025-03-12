N=int(input())

arr = [[0 for j in range(2)] for i in range(N)]

for i in range(N):
    arr[i][0],arr[i][1]=map(int,input().split())

arr.sort()

for i in range(N):print(arr[i][0],arr[i][1])