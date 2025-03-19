import sys
input = sys.stdin.readline
a,b = map(int,input().split())
result = 1

while True:
    if b==a:
        break
    elif b<=a:
        result=-1
        break
    result+=1

    if b%10 ==1:
        b=b//10
    elif b%2 ==0:
        b=b//2
    else:
        result=-1
        break
print(result)