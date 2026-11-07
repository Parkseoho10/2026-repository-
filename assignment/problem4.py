numbers = [12, 7, 19, 20, 33, 42, 8, 15, 26, 31]
count = 0
for i in numbers:
    if i % 2 == 0:
        count = count + 1
        print("짝수:", i)
    else:
        count = count
print(count,"개")