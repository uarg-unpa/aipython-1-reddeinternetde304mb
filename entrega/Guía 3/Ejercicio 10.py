num_1 = 0
num_2 = 0

while num_1 <= 6 and num_2 <=6:
    print(f"{num_1} {num_2}")
    num_2 += 1
    if num_2 > 6:
        num_1 += 1
        num_2 = num_1