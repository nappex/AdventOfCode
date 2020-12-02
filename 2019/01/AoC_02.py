sum = 0

with open("01/input", mode="r") as f:
    masses = f.readlines()
    for num in masses:
        num = int(num.strip())
        while num > 0:
            num = (num // 3) - 2
            if num > 0:
                sum += num

print(sum)
