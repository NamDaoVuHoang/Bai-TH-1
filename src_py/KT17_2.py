def merge(lst,l,mid,r):
    lst1 = lst[l:mid]
    lst2 = lst[mid:r]

    n1 = len(lst1)
    n2 = len(lst2)

    result = []

    i = 0
    j = 0

    done = False
    while not done :
        if lst1[i] < lst2[j] :
            result.append(lst1[i])
            i += 1
        else :
            result.append(lst2[j])
            j += 1
        if i == n1 or j == n2 :
            done = True
            break

    result.extend(lst1[i:])
    result.extend(lst2[j:])
    lst[l:r] = result


def mergeSort(lst,l,r) :
    if l < r-1 :
        mid = (l+r) // 2

        """ do trong python không hỗ trợ tham chiếu đến 1 đoạn trong list
        nên không được gán như trong ví dụ merge_sort.py """
        # chia dãy
        mergeSort(lst,l,mid)
        mergeSort(lst,mid,r)

        # trộn 2 dãy
        merge(lst,l,mid,r)

if __name__ == '__main__':
    lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    mergeSort(lst,0,len(lst))
    print(lst)
