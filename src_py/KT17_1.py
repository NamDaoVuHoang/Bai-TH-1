def binarySearch(lst, target):
    # lst đã sắp xếp tăng dần
    i = 0
    j = len(lst) - 1

    while i < j:
        # vị trí giữa
    	m = (i + j) // 2
        # phần tử ở m nhỏ hơn target thì tăng cận trái
    	if lst[m] < target:
    		i = m + 1
        # phần tử ở m lớn hơn target thì giảm cận phải
    	elif lst[m] > target:
    		j = m
    	else:
            return m

    if lst[i] == target :
        return i
    # nếu target không có trong lst
    else :
        return -1

l = [i for i in range(10)]
x = 6
position = binarySearch(l,x) + 1

if position != -1 and position != 0 :
    print("vi tri cua {} trong {} la {}".format(x,l,position))
else :
    print(x,"khong co trong {}".format(l))
