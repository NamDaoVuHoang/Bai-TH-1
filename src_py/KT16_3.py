# ví dụ 1 ở KT16_2

# ví dụ 2
print(' ví dụ 2:')
for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            print('%d la bang %d * %d' % (num, i, j))
            break
    else:
        print(num, 'la so nguyen to')

# ví dụ 3
print('\nví dụ 3:')
numPayCodes = [1, 2, 3, 4, 5]

numDivisions = [6, 7, 8, 9, 10]

summ = 0
# chưa định nghĩa summ
for i in numPayCodes:
    summ = summ + i
for j in numDivisions:
    summ = summ + j
    for i in numDivisions :
        summ = summ + i

print(summ)
