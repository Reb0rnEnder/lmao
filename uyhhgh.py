x: int = int(input("num to sqrt>"))
y: int = x
while y != 1:
    for z in range(2, x):
        if (y % z) != 0: continue
        print(f"{y} | {z}")
        y = y // z
        break
print("1 | 1")
