path = []
x, y = 0, 0
path.append((x, y))

while True:
    print("\n1:Up  2:Down  3:Left  4:Right  5:Show Path  6:Exit")
    ch = int(input("Choice: "))

    if ch == 1: y += 1
    elif ch == 2: y -= 1
    elif ch == 3: x -= 1
    elif ch == 4: x += 1
    elif ch == 5:
        print(path)
        continue
    elif ch == 6:
        break

    path.append((x, y))
