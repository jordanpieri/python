num = int(input("?:"))
steps = 0
c0 = num
while c0 != 1:
    if c0 % 2 != 0:
        c0 = c0 * 3 + 1

    if c0 % 2 == 0:
        c0 = c0 // 2

    steps = steps + 1
    print(c0)

if c0 == 1:
    print(c0, "Steps =", steps)
