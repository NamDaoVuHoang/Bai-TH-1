def insertionSort(a_list):
   for index in range(1, len(a_list)):

     # chọn một giá trị để chèn
     current_value = a_list[index]
     position = index

     # xác định vị trí cho phần tử được chèn
     while position > 0 and a_list[position-1] > current_value:
         a_list[position] = a_list[position-1]
         position = position - 1

     #chèn giá trị tại vị trí trên
     a_list[position] = current_value


if __name__ == '__main__':
    a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insertionSort(a_list)
    print(a_list)
