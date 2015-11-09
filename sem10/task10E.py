def searchLR(data, target):
	return (_searchL(data, target), _searchR(data, target))

def _searchL(data, target):
	first = 0
	last = len(data)

	while first < last:
		mid = first + (last - first)//2
		if target <= dataN[mid]:
			last = mid
		elif target > dataN[mid]:
			first = mid + 1

	if last < len(data) and data[last] == target:
		return last + 1
	else:
		return -1

def _searchR(data, target):
	first = 0
	last = len(data)

	while first < last:
		mid = first + (last - first)//2
		if target < dataN[mid]:
			last = mid
		elif target >= dataN[mid]:
			first = mid + 1

	if first < len(data) and data[first] == target:
		return first + 1
	else:
		return -1


N, M = tuple(map(int, input().split()))
dataN = list(map(int, input().split()))
dataM = list(map(int, input().split()))

for target in dataM:
	left, right = searchLR(dataN, target)
	if left != -1 and right != -1:
		print(left, right)
	else:
		print(0)

