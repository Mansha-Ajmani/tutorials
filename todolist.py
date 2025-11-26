tasks = []

while True:
    print("\n1:Add  2:View  3:Delete  4:Exit")
    ch = int(input("Choice: "))

    if ch == 1:
        t = input("Enter task: ")
        tasks.append(t)

    elif ch == 2:
        for i, t in enumerate(tasks):
            print(i, ":", t)

    elif ch == 3:
        idx = int(input("Index to delete: "))
        if 0 <= idx < len(tasks):
            tasks.pop(idx)

    elif ch == 4:
        break
