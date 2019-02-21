def isPrime(n):
    # kiểm tra tính nguyên tố của n
    # nếu n không chia hết cho số nào trong đoạn [2, sqrt(n)] thì return true
    return len(list(filter(
        # kiểm tra số các số 0 ở list sau dấu phẩy
        lambda x: x == 0,
        map(
            # In ra các số dư khi chia n cho y với y thuộc đoạn [2, sqrt(n)]
            lambda y: n % y, range(2, int(n**0.5)+1)
            )
        ))) == 0


# in ra các số nguyên tố nhỏ hơn 100
for i in range(2, 100):
    if isPrime(i):
        print(i)
