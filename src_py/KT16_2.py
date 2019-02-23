i = 2
while i < 100:
    if i == 2 or i == 3:
        print(i, " la so nguyen to")

    j = 2
    while j <= (i / j):
        if not i % j:
            break

        j += 1
        if j > i / j:
            print(i, " la so nguyen to")
    
    # i phải nằm ở vòng while ngoài
    i += 1

print("Good bye!")
