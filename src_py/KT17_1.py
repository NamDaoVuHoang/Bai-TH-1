def binarySearch(lst, target):
    i = 0
    j = len(lst) - 1
    while i < j:
    	m = (i + j) // 2
    	if lst[m] < target:
    		i = m + 1
    	elif lst[m] > target:
    		j = m
    	else:
    		return m
    if lst[i] == target :
        return i
    else :
        return -1

l = [i for i in range(10)]

position = binarySearch(l,6) + 1

if position != -1 :
    print("vi tri cua {} trong {} la {}".format(6,l,position))
else :
    print(6,"khong co trong {}")
