sz = int(input())
data = list(map(int, input().split()))
target = int(input())

number = data[0]
min_diff = abs(number - target)
for x in data[1:]:
	diff = abs(x - target)
	if  diff < min_diff:
		min_diff = diff
		number = x

print(number)
