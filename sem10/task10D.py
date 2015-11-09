N, K = tuple(map(int, input().split()))
dataN = list(map(int, input().split()))
dataK = list(map(int, input().split()))

for target in dataK:
	first = 0
	last = len(dataN)

	while first < last:
		mid = first + (last - first)//2
		if target < dataN[mid]:
			last = mid
		elif target > dataN[mid]:
			first = mid + 1
		else:
			print('YES')
			break
	else:
		print('NO')
