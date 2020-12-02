sum = 0

with open("input", mode="r") as f:
    masses = f.readlines()
    for num in masses:
        num = int(num.strip())
        sum += ((num // 3) - 2)

print(sum)
