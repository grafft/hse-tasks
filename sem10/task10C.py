sz = int(input())
data = list(map(int, input().split()))

min1 = min(data)
data.remove(min1)
min2 = min(data)

print(min1, min2)
