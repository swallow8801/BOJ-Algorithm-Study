def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start<= end :
        mid = (start + end) //2
        if data[mid] == target:
            return 1
        elif data[mid] < target:
            start = mid+1
        else:
            end = mid -1

    return 0

n = int(input())
n_list = list(map(int,input().split()))
n_list.sort()
m = int(input())
m_list = list(map(int,input().split()))

for i in m_list:
    answer = binary_search(i,n_list)
    print(answer)