num = int(input("?:"))
steps = 0
c0 = num
if num != 1:
    c0 = num
    while c0 % 2 != 0:
        c0 = c0 * 3 + 1
        steps = steps + 1
        print(c0)

    while c0 % 2 == 0:
        c0 = c0 // 2
        steps = steps + 1
        print(c0)

else:
    num == 1
    print(c0, "Steps =", steps)
